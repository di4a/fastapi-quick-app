from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'name':'Lucas'}