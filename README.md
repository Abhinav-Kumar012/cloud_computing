# Cloud computing course stuff

## setup
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## rest assignment
[todo app](todo_rest/)

## grpc assignments
[todo app](todo/) \
[chat app](chat/)

### grpc commands
```sh
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. chat.proto
```

## docker assigment
[todo app](todo_rest/)

### docker commands
```sh
docker build -f todo_rest/dockerfile -t flask-rest-api .
docker run --name todo-rest-api-flask -p 5000:5000 flask-rest-api:latest
```

