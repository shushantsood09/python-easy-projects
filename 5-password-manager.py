master_pwd = input("What is master password? ")

def view():
    pass

def add():
    name = input("Account name: ")
    pwd = input("Password :")

    #If open with file with the eith keyword there is no need to manually close the file. So, it is pretty much important. 
    with open('passwords.txt', 'a') as f:
        f.write(name +  "|" + pwd)

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == 'q':
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue