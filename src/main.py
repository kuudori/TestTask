from fastapi import FastAPI

from src.queue.router import router

app = FastAPI(title="test-task")

app.include_router(router)
