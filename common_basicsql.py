
import psycopg2


def connection_data_get():

    question_list = ["Please enter your database name:",
                     "Please enter your user name:",
                     "Please enter your host name:",
                     "Please enter your password:"]
    inputs = get_inputs(question_list)
    return inputs


def database_connect(inputs):

    connect_str = str("dbname='" + inputs[0] + "' user='" + inputs[1] + "' host='" + inputs[2] +
                      "' password='" + inputs[3] + "'")
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor


def get_inputs(question_list):
    inputs = []
    print("")
    for question in question_list:
        user_input = input(question)
        inputs.append(user_input)
    return inputs


def print_menu(title, list_options, exit_message):
    print(title)
    for option in enumerate(list_options):
        print("({0}) {1}".format(option[0] + 1, option[1]))
    print("({0}) {1}".format("0", exit_message))

