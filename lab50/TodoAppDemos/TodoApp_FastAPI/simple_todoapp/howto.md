## Resources:
https://fastapi.tiangolo.com/tutorial/

## Create project and virtenv:
```
mkdir simple_todoapp
cd simple_todoapp
python -m venv ./.venv

# activate virtualenv:
source ./venv/bin/activate
```

## Dependancy installations:
```

# Install FastAPI and Uvicorn for async web serving
pip install fastapi
pip install "uvicorn[standard]"

# Install packages for parsing multipart/form-data and Jinja2 for templates
pip install python-multipart jinja2

# Install SQLAlchemy for database interactions
pip install sqlalchemy

# Install sqlalchemy2-stubs for better type hinting with SQLAlchemy
pip install sqlalchemy2-stubs

```

## Project structure:
```
|simple_todoapp
└── src
    ├── app.py
    ├── db.py
    ├── models.py
    └── templates
        └── base.html
```

## Run the app:
`uvicorn app:app --reload`