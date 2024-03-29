FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1


RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY . /app/

CMD [ "python3", "manage.py" , "runserver", "0.0.0.0:7000"]
