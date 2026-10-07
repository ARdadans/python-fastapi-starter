FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src
ENV HOST=0.0.0.0
ENV PORT=8000
ENV RELOAD=false

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY run.py .

EXPOSE 8000

CMD ["python", "run.py"]
