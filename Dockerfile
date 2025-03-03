# Imagen base: Python - debian bookworm
FROM python:3.12-slim-bookworm

WORKDIR /fibonacci

COPY . .

RUN pip install --no-cache-dir --upgrade pip \
	&& pip install --no-cache-dir -r requirements.txt

CMD ["python","main.py"]
