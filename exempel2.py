import hashlib

# Filnamn
filename = "example.txt"

# Skapa en SHA-256 hash för filen
def sha256_hash_file(filepath):
    hash_sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        # Läs filen i små bitar för att undvika minnesproblem med stora filer
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_sha256.update(byte_block)
    return hash_sha256.hexdigest()

hash_value = sha256_hash_file(filename)
print(f"SHA-256 hash för filen '{filename}' är: {hash_value}")
