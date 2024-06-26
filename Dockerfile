FROM python:3.11-alpine3.19
LABEL authors="skiyman"

WORKDIR .

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "main:app", "--worker-class","uvicorn.workers.UvicornWorker"]
