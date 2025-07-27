from fastapi import APIRouter
from src.api.routes.books import router as books_router
from src.api.routes.API import router as api_router

main_router = APIRouter()

main_router.include_router(books_router, tags=["Books"])
main_router.include_router(api_router, prefix="/api", tags=["API"])