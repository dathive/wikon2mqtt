FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD . /app

# Ajouter uv au PATH
ENV PATH="/root/.cargo/bin:$PATH"

# Créer le répertoire de travail
WORKDIR /app

# Installer les dépendances
RUN uv sync

# Commande de lancement
CMD ["uv", "run", "main.py"]