from fastapi import FastAPI

from app.routes.interview import router

app = FastAPI(
    title="Archie Conversation Service"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "service": "Archie Conversation Service",
        "status": "running"
    }