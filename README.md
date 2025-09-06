# Cloud computing course stuff

## setup
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## grpc assignments
[todo app](todo/) \
[chat app](chat/)

### grpc commands
```sh
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. chat.proto
```
