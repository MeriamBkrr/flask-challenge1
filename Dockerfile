# Utilise une image Python légère
FROM python:3.11-slim

# Dossier de travail dans le container
WORKDIR /app

# Copie tous les fichiers du projet
COPY . .

# Installer Flask
RUN pip install flask

# Exposer le port 5000
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "app.py"]
