from cryptography.fernet import Fernet
    
def Encrypt(password, key):
    fernet = Fernet(key)
    EncPassword = fernet.encrypt(password.encode())
    print("Enc", EncPassword)
    return EncPassword

def Decrypt(password, key):
    fernet = Fernet(key)
    decMessage = fernet.decrypt(password).decode()
    print("Dec", decMessage)
    return decMessage