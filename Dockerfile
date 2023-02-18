FROM python:3.8-slim

LABEL maintainer="dockhardman <f1470891079@gmail.com>"

RUN python -m pip install --upgrade pip

# Install Dependencies
WORKDIR /
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt && pip list

# Application
WORKDIR /app/
COPY app /app

CMD ["sh", "/app/start.sh"]
