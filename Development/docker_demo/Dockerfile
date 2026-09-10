# 1. Base image — Python 3.11 without unnecessary extras
FROM python:3.11-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy and install dependencies FIRST (layer cache trick)
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. Copy the application code
COPY app.py .

# 5. Default command to run when the container starts
CMD ["python", "app.py"]
