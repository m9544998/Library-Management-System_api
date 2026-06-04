from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB = "library.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY,
        name TEXT,
        author TEXT
    )
    """)

    conn.commit()
    conn.close()

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO books VALUES (?, ?, ?)",
        (data["id"], data["name"], data["author"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Book Added"})

@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()

    conn.close()

    books = []
    for row in rows:
        books.append({
            "id": row[0],
            "name": row[1],
            "author": row[2]
        })

    return jsonify(books)
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "UPDATE books SET name=?, author=? WHERE id=?",
        (data["name"], data["author"], id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Book Updated"})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("DELETE FROM books WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return jsonify({"message": "Book Deleted"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)