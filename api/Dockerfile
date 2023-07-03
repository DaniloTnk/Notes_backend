FROM python:3.8-alpine

RUN apk update \
    && apk --no-cache --update add build-base

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app/backend/

COPY requirements.txt /app/backend/

RUN pip install --no-cache-dir -r requirements.txt 

COPY . /app/backend/
EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]