from fastapi import FastAPI

app=FastAPI(title="CI/CD Demo API")

@app.get("/")
def home():
    return {"message": "Welcome to CI/CD Practical"}

@app.get("/users")
def get_users():
    return[
        {"id":1,"name":"vishesh"},
        {"id":2,"name":"nirmit"}
    ]

@app.get("/health")
def health():
    return {"status":"healthy"}