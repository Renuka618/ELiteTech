from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (acts like a database)
books = [
    {"id": 1, "title": "Python Basics", "author": "John Doe"},
    {"id": 2, "title": "Web Development with Flask", "author": "Jane Smith"}
]

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Library API"})

# GET all books
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

# GET book by ID
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    return jsonify(book) if book else (jsonify({"error": "Book not found"}), 404)

# CREATE a new book
@app.route("/books", methods=["POST"])
def add_book():
    new_book = request.json
    new_book["id"] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

# UPDATE a book
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    
    data = request.json
    book.update(data)
    return jsonify(book)

# DELETE a book
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": "Book deleted"})

if __name__ == "__main__":
    app.run(debug=True)
