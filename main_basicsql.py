
import common_basicsql

def choose():
    inputs = get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        mentors_names = common_basicsql.mentors_names(cursor)
    elif option == "2":

    elif option == "3":

    elif option == "4":
    elif option == "5":
    elif option == "6":
    elif option == "7":
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["question 1",
               "question 2",
               "question 3",
               "question 4",
               "question 5",
               "question 6",
               "question 7"]

    print_menu("Main menu", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError:
            print('please choose a number from 0 to 7')



if __name__ == '__main__':
    main()

