from fastapi import APIRouter, FastAPI






app = FastAPI()





@app.get('/')
def index():
    
    return {"home": "Router"}