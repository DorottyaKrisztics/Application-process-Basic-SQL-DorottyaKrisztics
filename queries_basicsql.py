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


def another_girl(cursor):
    cursor.execute("""SELECT first_name || ' ' || last_name
                    AS full_name, phone_number
                    FROM applicants
                    WHERE email LIKE '%@adipiscingenimmi.edu';""")
    rows = cursor.fetchall()
    for row in rows:
        print(row[0] + " " + row[1])
    print("")


def new_applicant(cursor):
    cursor.execute("""DELETE
                    FROM applicants
                    WHERE  application_code='54823';""")
    cursor.execute("""INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                    VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', '54823');""")
    cursor.execute("""SELECT id, first_name, last_name, phone_number, email, application_code
                    FROM applicants
                    WHERE  application_code='54823';""")

    rows = cursor.fetchall()
    for row in rows:
        print(str(row[0]) + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[4] + " " + str(row[5]))
    print("")


def jemima_phone_number(cursor):
    cursor.execute("""UPDATE applicants
                    SET phone_number='003670/223-7459'
                    WHERE first_name='Jemima' AND last_name='Foreman';""")

    cursor.execute("""SELECT first_name, last_name, phone_number
                    FROM applicants
                    WHERE first_name='Jemima' AND last_name='Foreman';""")
    rows = cursor.fetchall()
    for row in rows:
        print(row[0] + " " + row[1] + " " + row[2])
    print("")

