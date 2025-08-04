from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def read_root():
    return {"message": " Hello !! Welcome to news page."}
