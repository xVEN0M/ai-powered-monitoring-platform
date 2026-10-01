from auth.hashing import hash_password, verify_password

password = "Hello123"

hashed = hash_password(password)

print("Original :", password)
print("Hashed   :", hashed)

print(
    "Verification:",
    verify_password(password, hashed)
)