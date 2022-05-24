FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir users
WORKDIR /users
COPY requirements.txt /users/
RUN pip install -r requirements.txt
COPY . /users/

