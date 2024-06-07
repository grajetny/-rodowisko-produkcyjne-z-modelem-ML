# Używamy obrazu python:3.11-slim-buster jako podstawy
FROM python:3.11-slim-buster

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy plik requirements.txt do katalogu roboczego
COPY requirements.txt .

# Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy pozostałe pliki aplikacji do katalogu roboczego
COPY . .

# Ustawiamy zmienną środowiskową dla Flask
ENV FLASK_APP=app

# Otwieramy port 5000
EXPOSE 5000

# Komenda uruchamiająca aplikację Flask
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
