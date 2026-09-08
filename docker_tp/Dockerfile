# 1. Image de base avec Python installé
FROM python:3.13-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# 2. Installer Flask
RUN pip install flask

# 3. Copier app.py dans l'image
COPY app.py .

# 4. Lancer app.py au démarrage du conteneur
CMD ["python", "app.py"]