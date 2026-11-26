FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY app/app.py ./app.py

EXPOSE 8080

USER nobody

CMD ["python", "app.py"]
