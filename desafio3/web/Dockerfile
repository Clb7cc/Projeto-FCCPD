FROM python:3.10

WORKDIR /app

COPY app.py /app/app.py
RUN pip install flask psycopg2 redis

EXPOSE 3000

CMD ["python", "app.py"]