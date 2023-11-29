from fastapi import FastAPI
from .scrapp import pages, screen

app = FastAPI()

@app.get('/pages')
def home_pages(page: str | None = 'browse'):
  data = pages(page)
  return data

@app.get('/movies')
def home_movies(page: int | None = 1):
  data = screen(page)
  return data