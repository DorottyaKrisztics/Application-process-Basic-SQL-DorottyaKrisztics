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
        pass
    elif option == "4":
        pass
    elif option == "5":
        pass
    elif option == "6":
        pass
    elif option == "7":
        pass
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Mentor's names",
               "Mentor's nicknames Miskolc",
               "question 3",
               "question 4",
               "question 5",
               "question 6",
               "question 7"]

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

