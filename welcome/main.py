from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/welcome")
def read_root():
    time.sleep(10)
    return {"message": " Hello !! Welcome to news page."}
