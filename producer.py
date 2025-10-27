#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Zadanie 2 - Producer
Program wysyłający dane na kolejkę RabbitMQ w formacie JSON.
"""

import pika
import json
import logging
from datetime import datetime

# Konfiguracja logowania
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(asctime)s - %(message)s',
    datefmt='%d.%m.%Y - %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Konfiguracja RabbitMQ
RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'przedmioty'

def get_user_input():
    """
    Pobiera dane od użytkownika.

    Returns:
        dict: Słownik z polami: nazwa_przedmiotu, liczba_ects, lista_ocen, data_godzina
    """
    print("\n=== Wprowadź dane przedmiotu ===")

    # Nazwa przedmiotu
    nazwa_przedmiotu = input("Podaj nazwę przedmiotu: ").strip()

    # Liczba ECTS
    while True:
        try:
            liczba_ects = int(input("Podaj liczbę punktów ECTS: "))
            if liczba_ects < 0:
                print("Liczba ECTS nie może być ujemna. Spróbuj ponownie.")
                continue
            break
        except ValueError:
            print("Nieprawidłowa wartość. Podaj liczbę całkowitą.")

    # Lista ocen
    print("Podaj listę ocen (oddzielone przecinkami, np. 5,4.5,3 lub zostaw puste):")
    oceny_input = input("Lista ocen: ").strip()

    lista_ocen = []
    if oceny_input:
        try:
            # Parsowanie ocen
            oceny_str = oceny_input.split(',')
            for ocena in oceny_str:
                ocena = ocena.strip()
                if ocena:
                    # Próba konwersji na float
                    lista_ocen.append(float(ocena))
        except ValueError as e:
            logger.warning(f"Błąd parsowania ocen: {e}. Używam pustej listy.")
            lista_ocen = []

    # Automatyczne dodanie daty i godziny
    data_godzina = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    # Utworzenie słownika z danymi
    data = {
        'nazwa_przedmiotu': nazwa_przedmiotu,
        'liczba_ects': liczba_ects,
        'lista_ocen': lista_ocen,
        'data_godzina': data_godzina
    }

    return data

def send_message(channel, data):
    """
    Wysyła wiadomość na kolejkę RabbitMQ.

    Args:
        channel: Channel RabbitMQ
        data (dict): Dane do wysłania
    """
    try:
        # Konwersja do JSON
        message = json.dumps(data, ensure_ascii=False, indent=2)

        # Wysłanie wiadomości
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=message,
            properties=pika.BasicProperties(
                content_type='application/json',
                delivery_mode=1  # Non-persistent
            )
        )

        logger.info(f"Send message to queue: {QUEUE_NAME}")
        logger.info(f"Message content: {data}")

    except Exception as e:
        logger.error(f"Error sending message: {e}")
        raise

def main():
    """Główna funkcja programu."""
    logger.info("Starting RabbitMQ Producer")

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

        # Pętla wysyłania wiadomości
        while True:
            try:
                # Pobranie danych od użytkownika
                data = get_user_input()

                # Wysłanie wiadomości
                send_message(channel, data)

                print("\nWiadomość została wysłana pomyślnie!")

                # Pytanie o kontynuację
                kontynuuj = input("\nCzy chcesz wysłać kolejną wiadomość? (t/n): ").strip().lower()
                if kontynuuj != 't':
                    break

            except KeyboardInterrupt:
                logger.info("Interrupted by user")
                break
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                kontynuuj = input("\nCzy chcesz spróbować ponownie? (t/n): ").strip().lower()
                if kontynuuj != 't':
                    break

    except pika.exceptions.AMQPConnectionError as e:
        logger.error(f"Could not connect to RabbitMQ: {e}")
        logger.error("Make sure RabbitMQ server is running")
    except KeyboardInterrupt:
        logger.info("Producer stopped by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        try:
            if 'connection' in locals() and connection.is_open:
                connection.close()
                logger.info("Connection closed")
        except:
            pass

    logger.info("Producer finished")

if __name__ == '__main__':
    main()
