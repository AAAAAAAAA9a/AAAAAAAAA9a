#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Zadanie 1 - Consumer
Program odbierający dane z kolejki RabbitMQ w formacie JSON
i zapisujący je do pliku CSV.
"""

import pika
import json
import csv
import logging
from datetime import datetime
import os

# Konfiguracja logowania
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(asctime)s - %(message)s',
    datefmt='%d.%m.%Y - %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Konfiguracja RabbitMQ
RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'testowa'
CSV_FILE = 'dane.csv'

def initialize_csv():
    """Tworzy plik CSV z nagłówkami jeśli nie istnieje."""
    file_exists = os.path.isfile(CSV_FILE)
    if not file_exists:
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['wiek', 'nazwisko', 'imie', 'jezyki_posortowane'])
        logger.info(f"Created CSV file: {CSV_FILE}")

def save_to_csv(data):
    """
    Zapisuje dane do pliku CSV.

    Args:
        data (dict): Słownik z polami: imie, nazwisko, wiek, jezyki_obce
    """
    try:
        # Sortowanie listy języków obcych
        jezyki_posortowane = sorted(data['jezyki_obce'])
        jezyki_str = '[' + ', '.join(jezyki_posortowane) + ']'

        # Zapis do CSV
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([
                data['wiek'],
                data['nazwisko'],
                data['imie'],
                jezyki_str
            ])

        logger.info(f"Saved to CSV: {data['imie']} {data['nazwisko']}, age {data['wiek']}")

    except Exception as e:
        logger.error(f"Error saving to CSV: {e}")

def callback(ch, method, properties, body):
    """
    Callback wywoływany przy odbiorze wiadomości z kolejki.

    Args:
        ch: Channel
        method: Method
        properties: Properties
        body: Treść wiadomości
    """
    try:
        logger.info(f"Received message from queue: {QUEUE_NAME}")

        # Parsowanie JSON
        data = json.loads(body)
        logger.info(f"Parsed JSON data: {data}")

        # Zapis do CSV
        save_to_csv(data)

        # Potwierdzenie odbioru wiadomości
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON format: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
    except KeyError as e:
        logger.error(f"Missing required field in JSON: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

def main():
    """Główna funkcja programu."""
    logger.info("Starting RabbitMQ Consumer")

    # Inicjalizacja pliku CSV
    initialize_csv()

    try:
        # Połączenie z RabbitMQ
        logger.info(f"Connecting to RabbitMQ at {RABBITMQ_HOST}")
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST)
        )
        channel = connection.channel()
        logger.info("Connected to RabbitMQ successfully")

        # Deklaracja kolejki
        channel.queue_declare(queue=QUEUE_NAME, durable=False)
        logger.info(f"Queue declared: {QUEUE_NAME}")

        # Konfiguracja consumera
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(
            queue=QUEUE_NAME,
            on_message_callback=callback,
            auto_ack=False
        )

        logger.info(f"Waiting for messages from queue: {QUEUE_NAME}")
        logger.info("Press CTRL+C to exit")

        # Rozpoczęcie nasłuchiwania
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError as e:
        logger.error(f"Could not connect to RabbitMQ: {e}")
        logger.error("Make sure RabbitMQ server is running")
    except KeyboardInterrupt:
        logger.info("Consumer stopped by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        try:
            if 'connection' in locals() and connection.is_open:
                connection.close()
                logger.info("Connection closed")
        except:
            pass

if __name__ == '__main__':
    main()
