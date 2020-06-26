FROM python:alpine

LABEL maintainer="https://github.com/alexsanderp"

RUN apk add --no-cache docker docker-compose
COPY . /app
RUN pip install -r /app/requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "/app/run.py"]
