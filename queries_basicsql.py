import psycopg2


def mentors_names(cursor):
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    rows = cursor.fetchall()
    print("The number of parts: ", cursor.rowcount)
    print("first name last name")
    for row in rows:
        print(row[0] + " " + row[1])
    print("")


def nick_names_miskolc(cursor):
    cursor.execute("""SELECT nick_name FROM mentors
                    WHERE city='Miskolc';""")

    rows = cursor.fetchall()
    print("The number of parts: ", cursor.rowcount)
    for row in rows:
        print(row[0])
    print("")


def carol(cursor):
    cursor.execute("""SELECT first_name || ' ' || last_name
                    AS full_name, phone_number
                    FROM applicants
                    WHERE first_name='Carol';""")
    rows = cursor.fetchall()
    for row in rows:
        print(row[0] + " " + row[1])
    print("")

