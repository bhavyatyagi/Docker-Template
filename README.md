# Docker-Template
This is a simple ReactJS-Flask application to mimic single system orchestration.

## How to Run?
1. Have repository locally by running ```git clone https://github.com/bhavyatyagi/Docker-Template.git```
2. Ensure you have docker-compose, if not then ```sudo apt-get docker-compose``` for linux or ```brew install docker``` on mac to install it.
3. Run ```docker-compose up```, you can add -d flag to run it in detached mode.
4. Both orchestrated containers up and running and you should be able to get backend_data on react front-end.

## To run containers individually
You can also run containers individually from individual Dockerfile to run client and server separately
- For Backend

  `docker run -it --rm -p 4000:4000 python-docker-template`
- For Frontend

  `docker run -it --rm -p 3000:3000 react-docker-template`
  
## To run servers locally
- For Backend

  1. `python install -r requirements.txt`
  2. `python -m flask run`
- For Frontend

  1. `npm i`
  2. `npm start`


> Any suggestions or comments to this repo are welcomed. Thank you for reading!
