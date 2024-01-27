# Usa un'immagine di base di Python
FROM python:3.8

# Imposta il work directory nell'immagine
WORKDIR /app

# Aggiorna pip
RUN pip install --upgrade pip

# Installa virtualenv
RUN pip install virtualenv

# Crea un ambiente virtuale nella directory /venv
# RUN virtualenv /venv

# Attiva l'ambiente virtuale
# llENV PATH="/venv/bin:$PATH"

# Definisci il comando di default per l'avvio del container
# CMD ["bash", "-c", "alias ll='ls -altr'"]

# Crea e attiva un ambiente virtuale
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Installa le dipendenze all'interno dell'ambiente virtuale
RUN pip install --upgrade pip \
    && pip install pelican beautifulsoup4 requests markdown

CMD ["bash"]
