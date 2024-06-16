import secrets
import string
import base64
#import pandas as pd
USER_DETAILS_FILEPATH = "password.txt"


def option():
    print("Generate a random password with RandPass!\n\nChoose an Option\n1. Generate Password\n2. Make your Password Secret\n3. Select 3 to Exit\n4. Find my Password\n")
    select = input("Select an Option ")
    if select == '1':
        generate_password()
    elif select == '2':
        Hash()
    elif select == '3':
        return
    elif select == "4":
        findkeyword()
    else:
        print("Invalid Choice!")
        option()

def generate_password():
    method = "Random"
    app = input("Input Keyword For this password? ")
    pwd = string.ascii_letters + string.digits + string.punctuation
    hashed_pwd = ''.join(secrets.choice(pwd) for _ in range(12))
    savepassword(app, hashed_pwd, method)
    print("Your Radom Password is:",hashed_pwd,"\nKeyword -",app,"\n!!Keep Safe!!")


def Hash():
    method = "Hashed"
    app = input("Input Keyword For this password? ")
    password = input("Input Password to Make Secret ")
    hashed_pwd = base64.b64encode(password.encode("utf-8"))
    deco = hashed_pwd.decode("utf-8")
    print("Password Hidden : ", hashed_pwd,"\nKeyword -",app)
    savepassword(app, hashed_pwd, method)
    

def savepassword(app, hashed_pwd, method):
    with open (USER_DETAILS_FILEPATH, "a") as f:
        f.write(f"{app}\t{hashed_pwd}\t{method}\n")

#View previous generated passwords

def findkeyword():
    key = input("Type Keyword to find Password: ")
    with open (USER_DETAILS_FILEPATH, "r") as f:
        found = False
        for line in f.readlines():
            parts = line.split(f'\t')
            if parts[0] == key:
                found = True
                print("Password Found! ==>",parts[1],"\nMethod ==>",parts[2])
                choice = input("Do You want to Unhide this Password? (y/n) ")
                if choice == "y":
                    decode(parts[1])
                if choice == "n":
                    return  
        if not found:
            print("Password not Found!\n")
                    

def decode(x):
    try:
        encoded = base64.b64encode(x)
        #xy=base64.b64decode(x.encode())
        #str_decoded = decoded.decode()
        decoded = base64.b64decode(encoded)
        print("Decoded Password: ", decoded)
    except (ValueError, base64.binascii.Error):
        print("Invalid base64 encoded string.")

def pwdgen():
    option()

