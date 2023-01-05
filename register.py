import csv
from IPython.display import clear_output


def registerUser():
    with open('users.csv', mode='a', newline='') as f:
        writer = csv.writer(f, delimiter=',')

        print('To register, please enter your info:')
        email = input('E-mail: ')
        password = input('Password: ')
        password2 = input('Re-type password: ')

        clear_output()

        if password == password2:
            writer.writerow([email, password])
            print('You are now registered!')
        else:
            print('Something went wrong. Try again.')
