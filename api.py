from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hola mundo dese fast api que no  compila pero si compila"}