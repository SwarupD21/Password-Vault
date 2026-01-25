# use for only encrypt() and decrypt() the password

from cryptography.fernet import Fernet
from django.conf import settings


# This line loads the master key
# Every encryption/decryption uses this
fernet = Fernet(settings.PASSWORD_ENCRYPTION_KEY)

def encrypt_password(plain_password:str) -> str:
    encrypted = fernet.encrypt(plain_password.encode())
    return encrypted.decode()
# User password is plain text (string)
# .encode() → converts text to bytes (computer language)
# fernet.encrypt() → scrambles it
# .decode() → converts back to string
# Returned value is safe to store in DB

def decrypt_password(encrypted_password: str) -> str:
    decrypted = fernet.decrypt(encrypted_password.encode())
    return decrypted.decode()