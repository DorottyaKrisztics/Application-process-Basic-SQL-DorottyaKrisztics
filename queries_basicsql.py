import psycopg2


def mentors_names(cursor):
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    rows = cursor.fetchall()
    print("The number of parts: ", cursor.rowcount)
    for row in rows:
        print(row[0] + " " + row[1])
    print("")