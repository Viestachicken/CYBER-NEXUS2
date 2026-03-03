FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Kita pake port 7860 karena itu jalur standar buat nembus Hugging Face Spaces
ENV PORT=7860
EXPOSE 7860
# Gunicorn bakal jagain AI Nexus lo tetep online 24/7 tanpa crash!
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
