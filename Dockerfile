# Imagen base: Python - debian bookworm
FROM python:3.12-slim-bookworm

COPY . .

CMD ["python","main.py"]
