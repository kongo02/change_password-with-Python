# import all necessary packages to be used
import csv
from IPython.display import clear_output

# handle user changing password


def changePassword():
    ''' 
        This function must confirm email and pass, then read data and save to local list
        because you cannot change a single value, you must save all data, then overwrite
        the entire file all together.
    '''

    email = input('Please confirm your e-mail: ')
    password = input('Please confirm your current password: ')

    emails = []
    passwords = []
    found = False

    with open('users.csv', mode='r') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if row == [email, password]:
                found = True
            elif row:
                emails.append(row[0])
                passwords.append(row[1])

    if found:
        new_pass = input('What would you like to change your password to? ')

        emails.append(email)
        passwords.append(new_pass)

        with open('users.csv', mode='w') as f:
            writer = csv.writer(f, delimiter=',')

            for i in range(len(emails)):
                writer.writerow([emails[i], passwords[i]])
    else:
        print('Sorry those credentials were incorrect.')
