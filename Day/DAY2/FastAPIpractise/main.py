from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "hello world","number": 123,"is fun":True}    