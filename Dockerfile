FROM python:3.10.12-alpine

LABEL authors="Gabriel Gonzales <jose.gabriel.gonzales.ramos@gmail.com>"

RUN addgroup -S deploy && adduser -S deploy -G deploy

WORKDIR /home/deploy/app

COPY --chown=deploy:deploy . .

RUN apk add --no-cache gpg unixodbc gcc g++ unixodbc-dev && pip3 install --no-cache-dir -r requirements.txt && \
    apk del gcc g++
    
USER deploy

EXPOSE 5005

ENTRYPOINT ["python3", "app.py"]