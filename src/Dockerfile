FROM python:3.10.5

WORKDIR /src

COPY ./requirements.txt /src/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["uvicorn", "router.main:app", "--reload","--host", "0.0.0.0", "--port", "8080"]