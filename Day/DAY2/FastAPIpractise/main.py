from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"page": "Home"}    

@app.get("/about")
def about():
    return {"page": "About","author": "Chakshu"}
@app.get("/health")
def contact():
    return {"status": "ok"}
#post request
@app.post("/create")
def create_something():
    return {"message":"created"}
