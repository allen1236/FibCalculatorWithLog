
# Fibonnaci Calculator with Log System

## Dependencies & Requirements

```bash
# Install protobuf compiler
$ sudo apt-get install protobuf-compiler

# Install buildtools
$ sudo apt-get install build-essential make

# Install python packages
$ pip3 install -r requirements.txt
```

## How to run

- Run the eclipse mosquitto docker container
```bash
$ cd rest/fibonnaci/mqtt
$ docker run -d -it -p 1883:1883 -v $(pwd)/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
```

- Compile and start gRPC service for fibonnaci
```bash
$ cd rest/fibonnaci/gRPC
# Compile protobuf schema to python wrapper
$ make
# Start the gRPC service (at localhost:8080)
$ python3 server.py
```
- Compile and start gRPC service for logging
```bash
$ cd rest/logs/gRPC
# Compile protobuf schema to python wrapper
$ make
# Start the gRPC service (at localhost:8888)
$ python3 server.py
```

- Run the django REST server
```bash
$ cd rest/
# Migrate database tables
$ python3 manage.py migrate
# Run the django rest server (at localhost:8000)
$ python3 manage.py runserver
```

## Using `curl` to perform client request

- Fibonnaci
```bash
$ curl -X POST http://localhost:8000/rest/fibonnaci -d '{"order": 10}'
```
- Logs
```bash
$ curl http://localhost:8000/rest/logs
```

## Using browser to perform client request

- Fibannaci: http://localhost:8000/rest/fibonnaci
- Logs: http://localhost:8000/rest/logs

## Demo Video
https://youtu.be/ek22DFLPYcY
