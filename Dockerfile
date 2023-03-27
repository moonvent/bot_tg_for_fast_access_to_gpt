FROM python:3.10

COPY . /code

WORKDIR /code


RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
