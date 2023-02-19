from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

from src.queue.router import router

app = FastAPI(title="test-task")

app.include_router(router)

@app.get("/docs", include_in_schema=False)
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API documentation")