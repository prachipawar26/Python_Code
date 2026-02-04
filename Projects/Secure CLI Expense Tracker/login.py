import getpass as gp
from credentials import userCred
from tracker import run_app

def login():
    print('Login')
    username = input('Enter the username: ')

    if gp.getpass('Enter the password: ').strip() == userCred.get(username):
        print('Successful Login')
        run_app(username)
        return True
    else:
        print('Login Failed!')
        return False
    
if __name__ == "__main__":
    login()