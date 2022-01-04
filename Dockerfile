FROM python:3.8.10-slim-buster

RUN apt-get update && apt-get install -y \
    python3-pip

RUN mkdir /opt/app
WORKDIR /opt/app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .

RUN chmod +x ./run.sh

CMD ["./run.sh"]
