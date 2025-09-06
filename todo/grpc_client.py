import grpc
import todo_pb2
import todo_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = todo_pb2_grpc.TodoServiceStub(channel)

        # Get the list of todos
        response = stub.GetTodoList(todo_pb2.Empty())
        print("Todo List:")
        for todo in response.todos:
            print(f"{todo.id}: {todo.title} - {'Done' if todo.completed else 'Pending'}")

        # Update the status of a todo
        update_response = stub.UpdateTodoStatus(todo_pb2.UpdateTodoRequest(id=1, completed=True))
        status = stub.AddTodoEntry(todo_pb2.Todo(id = 3,title = "take uno back",completed = False))
        print(update_response.message)
        print(status.completed)

if __name__ == '__main__':
    run()