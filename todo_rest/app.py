from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
todos = [
    {"id": 1, "task": "Buy groceries", "done": False},
    {"id": 2, "task": "Read a book", "done": True}
]

# GET all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# GET a specific todo
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    return jsonify(todo) if todo else ("Not Found", 404)

# POST a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = {
        "id": todos[-1]["id"] + 1 if todos else 1,
        "task": data["task"],
        "done": data.get("done", False)
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# PUT to update a todo
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()   
    for todo in todos:
        if todo["id"] == todo_id:
            todo["task"] = data.get("task", todo["task"])
            todo["done"] = data.get("done", todo["done"])
            return jsonify(todo)
    return ("Not Found", 404)

# DELETE a todo
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return ("Deleted", 204)

if __name__ == '__main__':
    app.run(debug=True)