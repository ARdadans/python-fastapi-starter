from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Python FastAPI Starter",
    version="1.0.0",
)


class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


class TodoCreate(BaseModel):
    title: str


# In-memory storage. Data is lost when the application restarts.
todos: list[Todo] = []


@app.get("/")
def root():
    return {"message": "Python FastAPI Starter", "status": "ok"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/api/todos", response_model=list[Todo])
def get_todos():
    return todos


@app.get("/api/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.post("/api/todos", response_model=Todo, status_code=201)
def create_todo(data: TodoCreate):
    next_id = max((todo.id for todo in todos), default=0) + 1
    todo = Todo(id=next_id, title=data.title)
    todos.append(todo)
    return todo


@app.delete("/api/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
