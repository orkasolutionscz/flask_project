FROM python:3.8

COPY requirements.pip /mdblog/requirements.pip
RUN pip install -r /mdblog/requirements.pip


COPY ./mdblog /mdblog

COPY ./configs/docker.py /mdblog/docker.py
COPY ./configs/uwsgi/docker_wsgi.ini /mdblog/docker_wsgi.ini

EXPOSE 80

ENV MDBLOG_CONFIG=/mdblog/docker.py

CMD ["uwsgi", "--ini", "/mdblog/docker_wsgi.ini"]
