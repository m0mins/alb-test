from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/welcome")
def read_root():
    # time.sleep(10)
    return {"message": " Hello !! Welcome to news page."}


# @app.get("/")
# def read_root():
#     time.sleep(10)
#     return {"message": " Hello !! Welcome to home page."}

# @app.get("/healthz")
# def health_check():
#     return {"status": "ok"}


is_healthy = False 

@app.get("/healthz")
def health_check():
    if is_healthy:
        return {"status": "healthy"}
    else:
        return Response(content='{"status": "unhealthy"}', status_code=500, media_type="application/json")

@app.get("/")
def home():
    return {"message": "Welcome to Home"}


@app.get("/toggle-health")
def toggle_health():
    global is_healthy
    is_healthy = not is_healthy
    return {"is_healthy": is_healthy}



# @app.get("/")
# def home():
#     if is_healthy:
#         return {"message": "Welcome to Home"}
#     else:
#         return Response(content='{"message": "Service is unhealthy"}', status_code=503, media_type="application/json")