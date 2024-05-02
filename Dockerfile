FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apk add --update pkgconfig mariadb-dev build-base gcc python3-dev linux-headers
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
CMD ["python3", "manage.py" , "runserver", "0.0.0.0:8000"]


# syntax=docker/dockerfile:1