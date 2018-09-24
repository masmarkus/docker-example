

FROM python:3

ADD ./docker-testing.py ./requirements.txt /usr/local/

RUN pip install -q --no-cache-dir --upgrade --upgrade-strategy=only-if-needed -r /usr/local/requirements.txt

WORKDIR /usr/local/

CMD [ "python", "./docker-testing.py" ]
