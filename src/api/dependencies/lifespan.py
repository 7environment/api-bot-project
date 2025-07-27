from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.config.constants import BASE_NODE_URL
import httpx

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http_client = httpx.AsyncClient(base_url=BASE_NODE_URL, timeout=10)
    yield

    if hasattr(app.state, "http_client") and app.state.http_client:
        await app.state.http_client.aclose()