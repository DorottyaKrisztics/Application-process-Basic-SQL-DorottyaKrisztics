import sys
import common_basicsql
import queries_basicsql


def choose(cursor):
    inputs = common_basicsql.get_inputs(["Please enter a number: "])
    option = inputs[0]
    if option == "1":
        queries_basicsql.mentors_names(cursor)
    elif option == "2":
        queries_basicsql.nick_names_miskolc(cursor)
    elif option == "3":
        queries_basicsql.carol(cursor)
    elif option == "4":
        queries_basicsql.another_girl(cursor)
    elif option == "5":
        queries_basicsql.new_applicant(cursor)
    elif option == "6":
        queries_basicsql.jemima_phone_number(cursor)
    elif option == "7":
        queries_basicsql.remove_applicants(cursor)
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Mentor's names",
               "Mentor's nicknames Miskolc",
               "Carol's name and phone number",
               "Another girl's name and phone number",
               "New applicant",
               "Jemima Forman's phone number",
               "Remove applicants"]

    common_basicsql.print_menu("Menu", options, "Exit program")


def main():
    inputs = common_basicsql.connection_data_get()
    cursor = common_basicsql.database_connect(inputs)
    while True:
        handle_menu()
        try:
            choose(cursor)
        except KeyError:
            print('please choose a number from 0 to 7')


if __name__ == '__main__':
    main()

