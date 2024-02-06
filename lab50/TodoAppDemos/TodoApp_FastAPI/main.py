from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import Union

app = FastAPI()

@app.get("/")
async def root():
  html_content = "<h1>Welcome to my site</h1>"
  return HTMLResponse(content=html_content, status_code=200)

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}