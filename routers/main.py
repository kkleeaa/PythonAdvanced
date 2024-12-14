from fastapi import FastAPI
from routers import authors, books, api_key
from database import create_database
from auth.security import get_api_key

app=FastAPI(
    title="BOOK management system",
    description= "An API from managing book, authors and genres",
    version="1.0.0"

)
@app.on_event("startup")
def startup_event():
    create_database()
app.include_router(authors.router, prefix="/api/authors", tags= ["Authors"])
app.include_router(books.router, prefix="/api/books", tags=["Books"])
app.include_router(api_key.router, prefix="/api/validate_key")

