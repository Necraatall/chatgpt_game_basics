FROM python:3.10-slim

# Nastavení pracovního adresáře
WORKDIR /app

# Instalace systémových závislostí
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    gcc \
    libasound-dev \
    && rm -rf /var/lib/apt/lists/*

# Kopírování Pipfile a Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# Instalace závislostí
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Kopírování aplikace
COPY app /app

# Nastavení příkazu pro spuštění
CMD ["pipenv", "run", "python", "app/main.py"]
