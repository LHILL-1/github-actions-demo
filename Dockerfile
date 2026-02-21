FROM python:3.12-slim

WORKDIR /app

# Copy and install dependencies first (better Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]
