import hashlib

# Originalsträng som ska hash-mappas
data = "Hello, world!"

# Skapa en sha512-hash av strängen
hash_object = hashlib.sha512(data.encode())
hash_hex = hash_object.hexdigest()

print(f"SHA-512 hash av strängen '{data}' är: {hash_hex}")
