FROM python:3.10.5

WORKDIR /src

COPY ./requirements.txt /src/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .