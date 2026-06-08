from fastapi import FastAPI

from app.routes.interview import router

app = FastAPI(
    title="Archie Conversation Service",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "service": "Archie Conversation Service",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }