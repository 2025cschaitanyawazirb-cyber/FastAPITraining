from fastapi import FastAPI
from pydantic import BaseModel
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
@app.get("/students/{usn}")
def get_result(usn: str):
    return { "result":"Distinction","usn": usn}
@app.get("/canidate/{roll_no}")
def get_canidate(roll_no: int):
    return { "result":"Distinction","roll_no": roll_no,"type": str(type(roll_no))}
#request bodies
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items")
def create_item(item: Item):
    return {"recieved_item": item,"total_price": item.price * 1.18}
