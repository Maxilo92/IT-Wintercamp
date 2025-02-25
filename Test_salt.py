import bcrypt

for i in range(10):
    salt = bcrypt.gensalt()
    print(salt)