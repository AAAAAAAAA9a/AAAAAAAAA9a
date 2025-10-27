# LAB 3 - RabbitMQ Data Processing

Projekt zawiera implementację dwóch zadań z laboratorium 3, związanych z przetwarzaniem danych przy użyciu RabbitMQ i pakietu pika.

## Struktura projektu

```
.
├── README.md                # Dokumentacja projektu
├── environment.yml          # Plik środowiska conda
├── requirements.txt         # Zależności pip
├── consumer.py              # Zadanie 1 - Consumer odbierający dane i zapisujący do CSV
├── producer.py              # Zadanie 2 - Producer wysyłający dane na kolejkę
└── test_publisher.py        # Skrypt testowy do zadania 1
```

## Wymagania

- Python 3.9+
- RabbitMQ Server
- Pakiet pika

## Instalacja

### Opcja 1: Użycie conda (zalecane)

```bash
conda env create -f environment.yml
conda activate rabbitmq-lab3
```

### Opcja 2: Użycie pip

```bash
pip install -r requirements.txt
```

## Instalacja RabbitMQ

### Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install rabbitmq-server
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server
```

### macOS (Homebrew):
```bash
brew install rabbitmq
brew services start rabbitmq
```

### Docker:
```bash
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

Interfejs webowy RabbitMQ będzie dostępny pod adresem: http://localhost:15672 (login: guest, hasło: guest)

## Zadanie 1 - Consumer (consumer.py)

### Opis
Program odbiera dane z kolejki RabbitMQ w formacie JSON i zapisuje je do pliku CSV.

### Format danych wejściowych
```json
{
  "imie": "Jan",
  "nazwisko": "Kowalski",
  "wiek": 30,
  "jezyki_obce": ["francuski", "angielski", "niemiecki"]
}
```

### Format pliku CSV
```csv
wiek;nazwisko;imie;jezyki_posortowane
30;Kowalski;Jan;[angielski, francuski, niemiecki]
```

### Użycie

1. Uruchom consumer (w osobnym terminalu):
```bash
python consumer.py
```

2. Program będzie czekał na wiadomości z kolejki `testowa`.

3. Aby wysłać testowe wiadomości, użyj skryptu testowego (w drugim terminalu):
```bash
python test_publisher.py
```

4. Dane zostaną zapisane do pliku `dane.csv`.

### Funkcje
- Automatyczne tworzenie pliku CSV z nagłówkami
- Sortowanie alfabetyczne listy języków obcych
- Logowanie wszystkich operacji z timestampem
- Obsługa błędów (nieprawidłowy JSON, brakujące pola)
- Potwierdzanie odbioru wiadomości (ACK/NACK)

## Zadanie 2 - Producer (producer.py)

### Opis
Program wysyła dane na kolejkę RabbitMQ w formacie JSON. Interaktywnie pyta użytkownika o dane przedmiotu i automatycznie dodaje timestamp.

### Użycie

```bash
python producer.py
```

Program poprosi o podanie:
1. Nazwa przedmiotu (tekst)
2. Liczba punktów ECTS (liczba całkowita)
3. Lista ocen (oddzielone przecinkami, np. `5,4.5,3` lub puste dla braku ocen)

### Przykładowa sesja
```
=== Wprowadź dane przedmiotu ===
Podaj nazwę przedmiotu: Matematyka
Podaj liczbę punktów ECTS: 6
Podaj listę ocen (oddzielone przecinkami, np. 5,4.5,3 lub zostaw puste):
Lista ocen: 5, 4.5, 4
```

### Format wiadomości wysyłanej
```json
{
  "nazwa_przedmiotu": "Matematyka",
  "liczba_ects": 6,
  "lista_ocen": [5.0, 4.5, 4.0],
  "data_godzina": "27.10.2025 14:30:45"
}
```

### Funkcje
- Interaktywne wprowadzanie danych
- Automatyczne dodawanie daty i godziny
- Walidacja wprowadzanych danych
- Możliwość wysłania wielu wiadomości bez ponownego uruchamiania
- Logowanie wszystkich operacji z timestampem

## Logowanie

Wszystkie programy logują kluczowe operacje w formacie:
```
INFO - DD.MM.YYYY - HH:MM:SS - Komunikat
```

Przykłady logów:
- `INFO - 27.10.2025 - 14:30:45 - Send message to queue: przedmioty`
- `INFO - 27.10.2025 - 14:30:46 - Received message from queue: testowa`
- `INFO - 27.10.2025 - 14:30:46 - Saved to CSV: Jan Kowalski, age 30`

## Testowanie

### Test Zadania 1
1. Uruchom consumer:
   ```bash
   python consumer.py
   ```

2. W drugim terminalu uruchom test publisher:
   ```bash
   python test_publisher.py
   ```

3. Sprawdź plik `dane.csv`:
   ```bash
   cat dane.csv
   ```

### Test Zadania 2
1. Uruchom producer:
   ```bash
   python producer.py
   ```

2. Wprowadź dane testowe

3. Możesz odbierać wiadomości używając interfejsu webowego RabbitMQ (http://localhost:15672) lub napisać dedykowany consumer

## Konfiguracja

### Consumer (consumer.py)
- `RABBITMQ_HOST`: Adres serwera RabbitMQ (domyślnie: `localhost`)
- `QUEUE_NAME`: Nazwa kolejki (domyślnie: `testowa`)
- `CSV_FILE`: Nazwa pliku CSV (domyślnie: `dane.csv`)

### Producer (producer.py)
- `RABBITMQ_HOST`: Adres serwera RabbitMQ (domyślnie: `localhost`)
- `QUEUE_NAME`: Nazwa kolejki (domyślnie: `przedmioty`)

## Rozwiązywanie problemów

### Błąd połączenia z RabbitMQ
```
Could not connect to RabbitMQ: ...
```
**Rozwiązanie**: Upewnij się, że serwer RabbitMQ jest uruchomiony:
```bash
sudo systemctl status rabbitmq-server
```

### Plik CSV nie jest tworzony
**Rozwiązanie**: Sprawdź uprawnienia zapisu w katalogu i logi aplikacji.

### Nieprawidłowy format JSON
**Rozwiązanie**: Upewnij się, że wiadomości wysyłane na kolejkę zawierają wszystkie wymagane pola.

## Autorzy

Projekt wykonany w ramach LAB 3.

## Licencja

MIT
