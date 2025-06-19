import random
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$_"
length=int(input("Enter the length of the password "))
password=""

for a in range(length):
  password+=random.choice(chars)
print(password)
