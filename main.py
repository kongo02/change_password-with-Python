from IPython.display import clear_output
from login import loginUser
from register import registerUser
from password import changePassword


# variables for main loop
active = True
logged_in = False


# main loop
while active:
    if logged_in:
        print('1. Logout\n2. Change Password\n3. Quit')
    else:
        print('1. Login\n2. Register\n3. Quit')

    choice = input('What would you like to do? ').lower()

    clear_output()

    if choice == 'register' and logged_in == False:
        registerUser()
    elif choice == 'login' and logged_in == False:
        logged_in = loginUser()
    elif choice == 'quit':
        active = False
        print('Thanks for using our software!')
    elif choice == 'logout' and logged_in == True:
        logged_in = False
        print('You are now logged out.')
    elif choice == 'change password' and logged_in == True:
        changePassword()
    else:
        print('Sorry, please try again!')
