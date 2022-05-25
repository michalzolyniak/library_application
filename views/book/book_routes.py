from flask import render_template, request, Blueprint
from database.datbase_connection import execute_sql
from constant.constants import DB_NAME

book_view = Blueprint('book_view', __name__, template_folder='./templates/books', static_folder='./static')


@book_view.route("/books", methods=(['GET']))
def get_books():
    """
        Get all books from table book
    """
    error = None
    sql = 'select * from book;'
    result = execute_sql(sql, DB_NAME, "select")
    if result:
        if result[0] == "Error":
            error = result[0] + " " + result[1]
    return render_template('books/books.html', error=error, books=result)


@book_view.route("/add_book", methods=(['GET', 'POST']))
def add_book():
    """
        Add a new book to the database
    """
    result = ""
    error = ""
    if request.method == 'GET':
        return render_template('books/add_book.html')
    elif request.method == 'POST':
        error = None
        isbn = request.form.get('isbn')
        name = request.form.get('name')
        description = request.form.get('description')
        sql = "Insert into book (isbn, Name, description) values (" + "'" + isbn + "'" \
              + "," + "'" + name + "'" + "," + "'" + description + "'" + ")"
        result = execute_sql(sql, DB_NAME, "insert")
        if result:
            if result[0] == "Error":
                error = result[0] + " " + result[1]
        else:
            result = "Book has been added to our database!"
    return render_template('books/finish.html', result=result, error=error)


@book_view.route("/book_details/<book_id>", methods=(['GET']))
def book_details(book_id):
    """
        Get from books database data corresponding to the id from url
        and display on the website
    """
    error = None
    sql = 'select * from book where id =' + book_id + ';'
    result = execute_sql(sql, DB_NAME, "select")
    if result:
        if result[0] == "Error":
            error = result[0] + " " + result[1]
    else:
        error = f"book id {book_id} doesn't exist in our database"
    return render_template('books/book.html', book=result, error=error)


@book_view.route("/delete_book<book_id>", methods=(['GET']))
def delete_book_data(book_id):
    """
        Remove from books database data corresponding to the book_id from url
    """
    sql = 'select * from book where id =' + book_id + ';'
    result = execute_sql(sql, DB_NAME, "select")
    error = None
    if result:
        if result[0] == "Error":
            error = result[0] + " " + result[1]
    else:
        error = f"book id {book_id} doesn't exist in our database"
    if not error:
        sql = 'delete from book where id =' + book_id + ';'
        result = execute_sql(sql, DB_NAME, "delete")
        if result:
            if result[0] == "Error":
                error = result[0] + " " + result[1]
        else:
            result = "Book has been deleted from our database"
    return render_template('books/finish.html', result=result, error=error)


@book_view.route("/loan_book", methods=(['GET', 'POST']))
def book_loan():
    """
        Loan a specific book from our database
    """
    result = ""
    error = ""
    if request.method == 'GET':
        error = None
        sql = "select name from book where is_loaned = 'f';"
        result = execute_sql(sql, DB_NAME, "select")
        if result:
            if result[0] == "Error":
                error = result[0] + " " + result[1]
        return render_template('books/loan_book.html', error=error, books=result)
    elif request.method == 'POST':
        error = None
        isbn = request.form.get('isbn')
        name = request.form.get('name')
        description = request.form.get('description')
        sql = "I into book (isbn, Name, description) values (" + "'" + isbn + "'" \
              + "," + "'" + name + "'" + "," + "'" + description + "'" + ")"
        result = execute_sql(sql, DB_NAME, "insert")
        if result:
            if result[0] == "Error":
                error = result[0] + " " + result[1]
        else:
            result = "Book has been added to our database!"
    return render_template('books/finish.html', result=result, error=error)
