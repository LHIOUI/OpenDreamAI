import diffusers
from fastapi import FastAPI

from app.core.config import settings
from app.routers import api_router

diffusers.logging.set_verbosity_error()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"/v1/{settings.SERVER_NAME}/openapi.json",
    debug=False,
    docs_url=f"/docs/{settings.SERVER_NAME}",
    redoc_url=f"/redoc/{settings.SERVER_NAME}",
    openapi_tags=settings.OPENAPI_TAGS,
)

app.include_router(api_router, prefix=f"/v1/{settings.SERVER_NAME}")