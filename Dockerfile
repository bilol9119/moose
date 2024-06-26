FROM python:3.10

WORKDIR /moose

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /moose/

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
