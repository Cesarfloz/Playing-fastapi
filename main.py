from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greeting():
    return f"Hi, this is my greeting"

@app.get("/about")
def about():
    return "I'm cesarfloz a python lover"

@app.get("/users/{user_id}")
def message(user_id):
    return f"Este es el perfil del usuario {user_id}"