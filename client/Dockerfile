FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir client
WORKDIR /client
COPY requirements.txt /client/
RUN pip install -r requirements.txt
COPY . /client/

