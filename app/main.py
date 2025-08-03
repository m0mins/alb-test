# from fastapi import FastAPI
# import socket

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": f"Hello from {socket.gethostname()}"}

# @app.get("/health")
# def health():
#     return {"status": "ok"}


from fastapi import FastAPI
import os
import time
import socket
app = FastAPI()

@app.get("/")
def read_root():
    port = os.getenv("APPPORT", "unknown")
    hostname = socket.gethostname()
    time.sleep(15)
    # return {"message": f"Hello from port {port}"}
    return {"message": f"Hello from {hostname} on port {port}"}

@app.get("/admin")
def read_root():
    port = os.getenv("APPPORT", "unknown")
    hostname = socket.gethostname()
    # time.sleep(15)
    # return {"message": f"Hello from port {port}"}
    return {"message": f"Hello Admin {hostname} on port {port}"}

@app.get("/app1")
def read_root():
    port = os.getenv("APPPORT", "unknown")
    hostname = socket.gethostname()
    # time.sleep(10)
    # return {"message": f"Hello from port {port}"}
    return {"message": f"Hello from {hostname} on port {port}"}

@app.get("/app2")
def read_root():
    port = os.getenv("APPPORT", "unknown")
    hostname = socket.gethostname()
    # return {"message": f"Hello from port {port}"}
    return {"message": f"Hello from {hostname} on port {port}"}


@app.get("/health")
def health():
    return {"status": "ok"}
