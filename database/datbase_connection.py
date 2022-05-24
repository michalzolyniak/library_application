from psycopg2 import connect, OperationalError

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"

def execute_sql(sql_code, db, oper_type):
    """
    Run given sql code with psycopg2.

    :param str sql_code: sql code to run
    :param str db: name of db,
    :param str oper_type: sql operation type: select, update, into
    :rtype: list
    :return: data from psycobg2 cursor as a list (can be None) if nothing to fetch.
    """
    # Place exercise 1 solution here.
    try:
        cnx = connect(
            user=USER,
            password=PASSWORD,  # coderslab  witaj123
            host=HOST,  # 'localhost'
            database=db
        )
        try:
            cursor = cnx.cursor()
            cursor.execute(sql_code)
            cnx.commit()
            if oper_type == "select":
                result = cursor.fetchall()
                cnx.close()
            else:
                result = []
            return result
        except Exception as e:
            cnx.close()
            result = ["Error", str(e)]
        return result
    except OperationalError as e:
        result = ["Error", str(e)]
        return result
