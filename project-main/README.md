## Development Environment
+ docker
+ python:3.9
+ mysql:8
+ nginx:1.21
+ flask:2.0.2
+ uwsgi:2.0.20
+ pymysqL:1.0.2


## How To Build Docker Environment

1. install docker: [ubuntu](https://docs.docker.com/engine/install/ubuntu/) / [windows and mac](https://docs.docker.com/engine/install/)
2. clone current gitlab repository
3. build docker images and run containers: `$ docker-compose up --build -d`
4. check running containers: `$ docker-compose ps`
5. visit web on `localhost`
6. remove running containers: `$ docker-compose down`


## How To Debug In Local Environment

**NOTE**
only `app` folder and its files **should be retouched**

1. clone current gitlab repository
2. run `__development.py`
3. visit web on `localhost:5000`