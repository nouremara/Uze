# Verwenden Sie ein offizielles Python-Image als Basis-Image
FROM python:3.8-slim-buster

# Setzen Sie die Arbeitsumgebung im Container auf /app
WORKDIR /app

# Kopieren Sie die aktuellen Verzeichnisinhalte in den Container unter /app
COPY . /app

# Installieren Sie alle benötigten Pakete
RUN pip install --no-cache-dir -r requirements.txt

# Legen Sie die Umgebungsvariablen fest (falls erforderlich)
# ENV NAME=Welt

# Führen Sie app.py aus, wenn der Container startet
CMD ["python", "app.py"]
