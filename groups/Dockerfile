FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir groups
WORKDIR /groups
COPY requirements.txt /groups/
RUN pip install -r requirements.txt
COPY . /groups/

