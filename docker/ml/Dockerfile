FROM python:3.9-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY embeddings embeddings
COPY app.py app.py

CMD ["gunicorn", "--bind=0.0.0.0:3000", "app:app"]
