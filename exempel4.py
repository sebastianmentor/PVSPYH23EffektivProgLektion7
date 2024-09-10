import hashlib
import os

def hash_password(password):
    # Generera en slumpmässig salt
    salt = os.urandom(16)
    print(salt.hex())
    # Hasha lösenordet med SHA-256 och salt
    hash_object = hashlib.sha256(salt + password.encode())
    return salt + hash_object.digest()

def verify_password(stored_password, provided_password):
    # Dela upp salt och hashvärde
    salt = stored_password[:16]
    stored_hash = stored_password[16:]
    # Hasha det angivna lösenordet med samma salt
    hash_object = hashlib.sha256(salt + provided_password.encode())
    return stored_hash == hash_object.digest()

# Exempelanvändning
hashed_pw = hash_password("my_secure_password")
print("Hashad version av lösenord:", hashed_pw.hex())

is_correct = verify_password(hashed_pw, "my_secure_password")
print("Lösenord korrekt:", is_correct)
