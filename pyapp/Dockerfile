FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src

ENTRYPOINT ["uvicorn", "src.main:app"]

CMD ["--host", "0.0.0.0", "--port", "3003", "--proxy-headers", "--reload"]
