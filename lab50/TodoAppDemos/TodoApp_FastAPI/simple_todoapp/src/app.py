from fastapi import FastAPI, Depends, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session
from db import SessionLocal, engine
import models

# Create database tables based on models
models.Base.metadata.create_all(bind=engine) #type:ignore

# Initialize Jinja2 templating engine
templates = Jinja2Templates(directory="templates")

# Create FastAPI application instance
app = FastAPI()

# Dependency for database access
def get_db():
    db = SessionLocal()
    try:
        return db  # Provide the database session
    finally:
        db.close()  # Ensure database session is closed properly

# Routes
# http://127.0.0.1:8000/
@app.get("/")
async def home(req: Request, db: Session = Depends(get_db)):
    # Retrieve all todos from the database
    todos = db.query(models.Todo).all()

    # Render the base.html template with context
    return templates.TemplateResponse("base.html", {"request": req, "todo_list": todos})

@app.post("/add")
def add(req: Request, title: str = Form(...), db: Session = Depends(get_db)):
    # Create a new Todo item based on the provided title
    new_todo = models.Todo(title=title)

    # Add the new todo to the database and commit changes
    db.add(new_todo)
    db.commit()

    # Redirect to the home page after successful creation
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/update/{todo_id}")
def update(req: Request, todo_id: int, db: Session = Depends(get_db)):
    # Retrieve the todo with the specified ID
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first() # type: ignore

    # Toggle the completion status of the todo and commit changes
    todo.complete = not todo.complete
    db.commit()

    # Redirect to the home page after successful update
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)



@app.get("/delete/{todo_id}")
def delete(req: Request, todo_id: int, db: Session = Depends(get_db)):
    # Retrieve the todo with the specified ID
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first() # type: ignore

    # Delete the todo from the database and commit changes
    db.delete(todo)
    db.commit()

    # Redirect to the home page after successful deletion
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
