from cryptography.fernet import Fernet
import getpass
import os.path
import os

cwd = os.getcwd()  # current directory
os.chdir(cwd)

# DIRECTORY PATH
file_path = cwd + "/database/"

# PASSWORD KEY STORING PATH
file_key_path = file_path + "passAuthKey.key" #hashing key

# USERS PASSWORD STORING DB PATH
file_users_db_path = file_path + "passwordAuth.txt"

if (os.path.exists(file_path) == False):
    os.mkdir(file_path)


def write_key():
    key = Fernet.generate_key()
    with open(file_key_path, 'wb') as key_file:
        key_file.write(key)

if (os.path.exists(file_key_path) == False):
    write_key()


def load_key():
    with open(file_key_path, 'rb') as f:
        key = f.read()
    return key


key = load_key()
fer = Fernet(key)

# To add and view the database------------------------------------------------------


def add():
    user = input('User: ')
    pwd = input('Password: ')

    with open(file_users_db_path, 'a') as f:
        f.write(user+'|'+fer.encrypt(pwd.encode()).decode()+'\n')


# def view():

#     user, passwd = "", ""

#     with open(file_users_db_path, 'r') as f:

#         for line in f.readlines():
#             data = line.rstrip()
#             user, passwd = data.split('|')
#             print('User: ' + user + '| Password: ' +
#                   fer.decrypt(passwd.encode()).decode())


def login():
    name = input("Enter UserName: ")
    passwd = getpass.getpass("Enter Password: ")
    with open(file_users_db_path, 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passwrd = data.split('|')
            if (user == name):
                if (fer.decrypt(passwrd.encode()).decode() == passwd):
                    print('Correct Password :)')
                    break
                else:
                    print("Wrong Password -_-")
                    break
    if (user != name):           
        print('Wrong Username Try Again :(')


while True:

    choice = input(
        'Would you wanna add a new Password or Login(add/ login / quit): ').lower()

    if choice == 'quit':
        break
    elif choice == 'add':
        add()
    # elif choice == 'view':
    #     view()
    elif choice == 'login':
        login()

    else:
        print('Wrong choice! Try Again -_-')