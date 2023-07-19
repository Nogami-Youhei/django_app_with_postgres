FROM python:3.10
USER root

RUN apt-get update
RUN apt-get install -y locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN apt-get install -y libpq-dev
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

WORKDIR /workdir
WORKDIR /workdir/opt/
COPY requirements.txt /workdir
RUN pip install -r /workdir/requirements.txt

#CMD python manage.py runserver 0.0.0.0:8000
#CMD uwsgi --http :8000 --module for_myapp.wsgi
#CMD uwsgi --ini uwsgi.ini