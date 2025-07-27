from  fastapi import FastAPI

app = FastAPI()

BOOKS =[
    {"title":"Title one","authour":"Author One", "category":"Category One"},
    {"title":"Title two","authour":"Author One", "category":"Category two"},
    {"title":"Title three","authour":"Author One", "category":"Category One"},
]

@app.get("/get-all-books")
def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
def read_book(book_title):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return  book

@app.get("/books/")
def read_category_by_query(category):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return  books_to_return
