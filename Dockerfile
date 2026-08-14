FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5009

<<<<<<< HEAD
CMD ["gunicorn", "--bind", "0.0.0.0:5003", "app:app"]
=======
CMD ["gunicorn", "--bind", "0.0.0.0:5009", "app:app"]
>>>>>>> 28eb8a73d835c2e95a2196e7f3778d0eebdbe6fc
