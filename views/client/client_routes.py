from flask import render_template, request, Blueprint
from database.datbase_connection import execute_sql
from constant.constants import DB_NAME

client_view = Blueprint('client_view', __name__, template_folder='./templates', static_folder='./static')


@client_view.route("/clients", methods=(['GET']))
def get_clients():
    """
        Get all clients from  table client
    """
    error = None
    sql = 'select * from client;'
    result = execute_sql(sql, DB_NAME, "select")
    if result:
        if result[0] == "Error":
            error = result[0] + " " + result[1]
    return render_template('client/clients.html', error=error, clients=result)


@client_view.route("/add_client", methods=(['GET', 'POST']))
def add_client():
    """
        Add a new client to the database
    """
    result = ""
    error = ""
    if request.method == 'GET':
        return render_template('books/add_client.html')
    elif request.method == 'POST':
        error = None
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        sql = "Insert into client (first_name, last_name) " \
              "values (" + "'" + first_name + "'" \
              + "," + "'" + last_name + "'" + ")"
        result = execute_sql(sql, DB_NAME, "insert")
        if result:
            if result[0] == "Error":
                error = result[0] + " " + result[1]
        else:
            result = "Client has been added to our database!"
    return render_template('client/finish.html', result=result, error=error)
