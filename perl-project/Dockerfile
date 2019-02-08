FROM python:3.7.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /task
WORKDIR /task
COPY requirements.txt /task/
RUN pip install -r requirements.txt
COPY . /task/