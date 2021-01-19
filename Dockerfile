FROM python:3

WORKDIR /app

COPY . .

RUN pip install flask flask_wtf wtforms

EXPOSE 5000

CMD ["python", "./server.py"]