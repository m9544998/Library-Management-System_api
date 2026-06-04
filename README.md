
# Library Management System API

## Description

This project is a Library Management REST API built using Flask and SQLite.

## Features

* Add Book
* View Books
* Update Book
* Delete Book

## Technologies

* Python
* Flask
* SQLite

## How To Run

1. Install Flask

pip install flask

2. Run Project

python app.py

3. Open Thunder Client

Base URL:

http://127.0.0.1:5000

## Endpoints

POST /books

GET /books

PUT /books/<id>

DELETE /books/<id>

# OUTPUT
```Thunder Client
Add Book

POST

http://127.0.0.1:5000/books

Body:

{
  "id": 1,
  "name": "Python",
  "author": "Ali"
}
Get Books

GET

http://127.0.0.1:5000/books

```
## Database

SQLite database file:

library.db

## Architecture

Thunder Client/Terminal
↓
Flask REST API
↓
SQLite Database

## Author

Maheen Asad
