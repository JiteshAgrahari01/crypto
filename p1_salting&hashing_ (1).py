import bcrypt
password = input("Enter Any Password: ")
# converting password to array of bytes
bytePwd = password.encode('utf-8')
# Generate salt
mySalt = bcrypt.gensalt()
# Hash password
hashed = bcrypt.hashpw(bytePwd, mySalt)
print(f"Hash Value of {password} is: \n{hashed}")
# checking password
checkpass = password
checkpass = checkpass.encode('utf-8')
res = bcrypt.checkpw(checkpass, hashed)
print(password)
