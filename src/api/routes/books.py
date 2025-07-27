from fastapi import APIRouter, HTTPException
from src.api.schemas.books import Book, NewBook

router = APIRouter()

books = [
    Book(
        id = 1,
        title = "Something about void",
        author = "Artyom"
    )
]

@router.get("/books", response_model=list[Book])
async def get_books() -> list[Book]:
    return books

@router.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    else:
        raise HTTPException(status_code=404, detail="Book not found")

@router.post("/books", response_model=Book)
async def create_book(book: NewBook) -> Book:
    new_book = Book(id=len(books)+1, title=book.title, author=book.author)
    books.append(new_book)
    return new_book