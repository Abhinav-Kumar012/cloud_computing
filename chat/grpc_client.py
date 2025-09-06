import grpc
import chat_pb2
import chat_pb2_grpc

def take_input():
    while(True):
        x = str(input())
        yield chat_pb2.ChatRequest(message = x)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = chat_pb2_grpc.ChatServiceStub(channel)
        reply_iter = stub.ChatStream(take_input())
        for reply in reply_iter:
            print(reply.reply)

if __name__ == '__main__':
    run()