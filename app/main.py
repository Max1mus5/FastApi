from fastapi import FastAPI
from .scrapp import pages

app = FastAPI()

@app.get('/pages')
def home_pages(page: str | None = 'browse'):
  data = pages(page)
  return data

@app.get('/series')
def news( page: str | None='world', category: str | None ='africa'):
  return {"SERIES"}