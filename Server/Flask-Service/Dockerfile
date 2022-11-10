FROM python:3.8.5-slim-buster

# Set the working directory to /Flask-Service
WORKDIR /Flask-Service

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 4000
CMD [ "python3", "-m" , "flask", "run", "--port=4000", "--host=0.0.0.0"]