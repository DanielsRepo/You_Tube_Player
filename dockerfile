FROM python:3.8

WORKDIR /player

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# ENTRYPOINT ["sh", "docker-entrypoint.sh"]
