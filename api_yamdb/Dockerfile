FROM python:3.7-slim
ENV TZ=UTC
WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY . .

RUN python manage.py collectstatic --no-input

CMD bash -c "python manage.py makemigrations && python manage.py migrate && gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000"
