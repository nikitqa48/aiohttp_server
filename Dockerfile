FROM python:3.12.1

EXPOSE 8080

WORKDIR /app

COPY . /app

RUN pip install poetry

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN chmod +x /app/start.sh

CMD ["sh", "/app/start.sh"]

