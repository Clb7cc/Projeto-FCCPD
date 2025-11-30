FROM python:3.10

WORKDIR /app

COPY app.py .

RUN pip install flask requests

EXPOSE 5002

CMD ["python", "app.py"]