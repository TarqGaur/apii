from fastapi import FastAPI
app = FastAPI()

# @app.get("/")
# def root():
#     return {"Hello":"1"}   

items = []
@app.post("/newpoint")
def newrequest(req:str):
    items.append(req)
    print (items)
    return items
