import getpass
database={"Ramu Kaka":"123456","Binod":"Binod","Munna Bhaiya":"BossDK"}
uid=input("Enter UserName: ")
passwrd=getpass.getpass("Enter Password: ")
for i in database.keys():
    if uid==i:
        while passwrd!=database.get(i):
            passwrd=getpass.getpass("Incorrect Passsword ,Try again")
        if passwrd==database.get(i):
            print("Correct Password")
        exit()
print("Invalid User Name")
