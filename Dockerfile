# 1) Base OS + Python
FROM python: 3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt


# 5) Commande de lancement
CMD ["python3","app.py"]
