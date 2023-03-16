FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]