#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test Publisher - do testowania consumer.py (Zadanie 1)
Wysyła przykładowe dane w formacie wymaganym przez zadanie 1.
"""

import pika
import json
import logging

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

# Przykładowe dane do wysłania
test_messages = [
    {
        "imie": "Jan",
        "nazwisko": "Kowalski",
        "wiek": 30,
        "jezyki_obce": ["francuski", "angielski", "niemiecki"]
    },
    {
        "imie": "Anna",
        "nazwisko": "Nowak",
        "wiek": 25,
        "jezyki_obce": ["angielski", "hiszpański"]
    },
    {
        "imie": "Piotr",
        "nazwisko": "Wiśniewski",
        "wiek": 35,
        "jezyki_obce": ["niemiecki", "rosyjski", "angielski", "chiński"]
    }
]

def send_test_messages():
    """Wysyła testowe wiadomości na kolejkę."""
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

        # Wysłanie wszystkich testowych wiadomości
        for i, data in enumerate(test_messages, 1):
            message = json.dumps(data, ensure_ascii=False, indent=2)

            channel.basic_publish(
                exchange='',
                routing_key=QUEUE_NAME,
                body=message,
                properties=pika.BasicProperties(
                    content_type='application/json',
                    delivery_mode=1  # Non-persistent
                )
            )

            logger.info(f"Send message {i}/{len(test_messages)} to queue: {QUEUE_NAME}")
            logger.info(f"Message: {data['imie']} {data['nazwisko']}")

        print(f"\nWysłano {len(test_messages)} testowych wiadomości!")

        # Zamknięcie połączenia
        connection.close()
        logger.info("Connection closed")

    except pika.exceptions.AMQPConnectionError as e:
        logger.error(f"Could not connect to RabbitMQ: {e}")
        logger.error("Make sure RabbitMQ server is running")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

if __name__ == '__main__':
    logger.info("Starting Test Publisher")
    send_test_messages()
    logger.info("Test Publisher finished")
