import grpc
from concurrent import futures
import todo_pb2
import todo_pb2_grpc

class TodoService(todo_pb2_grpc.TodoServiceServicer):
    def __init__(self):
        self.todos = [
            todo_pb2.Todo(id=1, title="Buy groceries", completed=False),
            todo_pb2.Todo(id=2, title="Write report", completed=False),
        ]

    def GetTodoList(self, request, context):
        return todo_pb2.TodoListResponse(todos=self.todos)

    def UpdateTodoStatus(self, request, context):
        for todo in self.todos:
            if todo.id == request.id:
                todo.completed = request.completed
                return todo_pb2.UpdateTodoResponse(message="Todo updated successfully")
        return todo_pb2.UpdateTodoResponse(message="Todo not found")
    
    def AddTodoEntry(self, request, context):
        for todo in self.todos:
            if todo.id == request.id :
                return todo_pb2.AddStatusTodo(completed = False)
        self.todos.append(request)
        return todo_pb2.AddStatusTodo(completed = True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

