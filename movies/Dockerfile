FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir movies
WORKDIR /movies
COPY requirements.txt /movies/
RUN pip install -r requirements.txt
COPY . /movies/

