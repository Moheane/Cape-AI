FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ENV PORT=8000

RUN mkdr /app 

ADD . /app

COPY .requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
    apt-get clean && \
    rm-rf /var/lib/apt/list/*

RUN pip install --upgrade pip
RUN pip install pipenv

RUN pipenv install --skip-lock --system --dev

RUN docker pull nginx


EXPOSE 8000


RUN pip install -r requirements.txt

COPY . /app
