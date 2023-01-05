import csv
from IPython.display import clear_output


def loginUser():
    print('To login, please enter your info:')
    email = input('E-mail: ')
    password = input('Password: ')

    clear_output()

    with open('users.csv', mode='r') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if row == [email, password]:
                print('You are now logged in!')
                return True

    print('Something went wrong, try again.')
    return False
