# Utilise une image Python légère
FROM python:3.11-slim

# Dossier de travail dans le container
WORKDIR /app

# Copie tous les fichiers du projet
COPY . .

# Installer Flask et PyMongo
RUN pip install --no-cache-dir flask pymongo

# Exposer le port 5000 pour Flask
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "app.py"]

