import grpc
from concurrent import futures
import chat_pb2
import chat_pb2_grpc


class ChatService(chat_pb2_grpc.ChatServiceServicer):
    """Missing associated documentation comment in .proto file."""
    def __init__(self):
        self.replies = {
            "hi" : "Hello",
            "what are you doing?" : "nothing",
            "how are you?" : "I'm fine"
        }

    def ChatStream(self, request_iterator, context):
        for req in request_iterator:
            t = req.message.lower()
            p = self.replies.get(t)
            if(t == "bye"):
                break
            elif p is None:
                yield chat_pb2.ChatResponse(reply="I don't know")
            else:
                yield chat_pb2.ChatResponse(reply=p)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()