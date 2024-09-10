import hashlib

# Originalsträng som ska hash-mappas
data = "Hello, world!"
# data = b"Hello, world!"

# Skapa en sha256-hash av strängen
hash_object = hashlib.sha256(data.encode())
hash_hex = hash_object.hexdigest()

print(f"SHA-256 hash av strängen '{data}' är: {hash_hex}")
