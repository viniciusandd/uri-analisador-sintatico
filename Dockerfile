FROM python:3.8.1-alpine3.11

WORKDIR /var/www/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD flask run -h 0.0.0.0 -p 5000