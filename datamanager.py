import private_connection
import psycopg2


def connection():

    try:
        connect_str = private_connection.private_connection()
        connection = psycopg2.connect(dbname=connect_str["dbname"],
                                      user=connect_str["user"],
                                      host=connect_str["host"],
                                      password=connect_str["password"])
        connection.autocommit = True
        cursor = connection.cursor()
        return cursor

    except psycopg2.DatabaseError as exception:
        print(exception)

#  psycopg2.InterfaceError: cursor already closed
    #finally:
        #if connection:
            #connection.close()


def run_query(query):
    cursor = connection()
    cursor.execute(query)
    query_list = cursor.fetchall()
    return query_list

