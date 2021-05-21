# set base image (host OS)
FROM python:3.8

WORKDIR /code

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 127.0.0.1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]