from flask import Flask
from views.book.book_routes import book_view
from views.client.client_routes import client_view

app = Flask(__name__)
app.register_blueprint(book_view)
app.register_blueprint(client_view)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


if __name__ == "__main__":
    app.run(debug=True)
