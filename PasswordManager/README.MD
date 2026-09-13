# Password Manager


- 'main.py is the login page
- 'portal.py' contains the 2 main functions of this project: adding password and viewing password
- 'storage.py' contains the database logic
- 'encrypt.py' contains the encryption of credentials code, using Fernet

What does this do ?

# Anchor paths to this script's folder instead of the current working
# directory, so the key file is always found/created in the same place
# no matter where you launch `python main.py` from.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.join(BASE_DIR, "secret.key")

- It makes sure the secret.key its in the same folder with the main.py, because you may run the command to run the folder from another folder, which may cause another secret.key making, then when secret.key is needed the code cant find or it may find 2 at the same time causing a clash.




https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
