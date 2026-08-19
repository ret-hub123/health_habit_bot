FROM python:3.11

WORKDIR /app



RUN apk add --no-cache \
    gcc \
    musl-dev \
    libpq-dev \
    postgresql-client \
    uwsgi \
    uwsgi-python3

COPY requirements.txt .


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN ls -la /app
RUN ls -la /app/habit_tracker

EXPOSE 8080

CMD ["uwsgi", "--ini", "uwsgi.ini"]