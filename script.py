import gnupg

#directory for gpg core files
gpg = gnupg.GPG(gnupghome='/Users/abis/.gnupg')

def Verify(): #to verify records and signs
    location_input = input("Enter path to file: ")
    file_data = open(str(location_input), "rb")
    veri = gpg.verify_file(file_data) 
    if not veri: raise ValueError("Signature not verified")
    else: print("Signature Verified")

def Record(): # to sign and record data
    location_input = input("Enter path to file: ")
    file_data = open(str(location_input), "rb")
    signed_data = gpg.sign_file(file_data) 
    print(signed_data)

def ImportKey():
    serverinput = input("Enter server name: ")
    keyIDinput = input("Enter keyID: ")
    import_result = gpg.recv_keys(str(serverinput),str(keyIDinput))
    print(import_result)
    print("Key Imported")

def SearchKey():
    email_input = input("Enter email ID: ")
    serverinput = input("Enter server name: ")
    a = gpg.search_keys(str(email_input),str(serverinput))
    print(a)

def SendKey():
    keyIDinput = input("Enter keyID: ")
    serverinput = input("Enter server name: ")
    b = gpg.send_keys(str(serverinput),str(keyIDinput))
    print(b)
    print("Key sent")

def EncryptData():
    location_input = input("Enter path to file: ")
    file_data = open(str(location_input), "rb")
    recp = "" #add recp
    encrypted = gpg.encrypt_file(str(file_data),recp) 
    print(encrypted)
    print("Data Encrypted")

def DecryptData():
    location_input = input("Enter path to file: ")
    file_data = open(str(location_input), "rb")
    decrypted = gpg.decrypt_file(file_data)
    print(decrypted)
    print("Data Decrypted")

user_input = input("Select Mode 1)Record 2)Verify 3)Import Key 4)Search Key 5)Send Key 6)Encrypt: 7)Decrypt: ")

if int(user_input) == 1:
    Record()
elif int(user_input) == 2:
    Verify()
elif int(user_input) == 3:
    ImportKey()
elif int(user_input) == 4:
    SearchKey()
elif int(user_input) == 5:
    SendKey()
elif int(user_input) == 6:
    EncryptData()
elif int(user_input) == 7:
    DecryptData()
else:
    print("Error")

# This whole program is written in refrence to this page https://docs.red-dove.com/python-gnupg/#decryption





