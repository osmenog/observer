FROM python:3.9-alpine

# set work directory
WORKDIR /app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./app/

RUN update-ca-certificates && \
    apk update && \
    apk add curl jq && \
    apk add --virtual build-deps gcc python3-dev musl-dev

RUN pip install --upgrade pip \
 && pip install -r ./app/requirements.txt

RUN apk del build-deps

# copy project
COPY ./observer /app/observer

CMD ["python", "-m", "observer"]