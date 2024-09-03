from cryptography.fernet import Fernet


# Function to load the key.
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

# key + password + text to encrypt = random text
# random text + key + password = text to encrypt

# Function to create the key

'''
def write_Key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

# write_Key() Function for calling write key.
# write_key()


# To encrpyt the password we need to install the module.

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            # For example
            # user1|abc
            # So, user = user1
            # passw = abc
            print("User:", user, "Pass:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    # If open with file with the eith keyword there is no need to manually close the file. So, it is pretty much important.
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode()+ "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == 'q':
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
