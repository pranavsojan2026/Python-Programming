import random

password="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv1234567890!@#$%&*"
password_length=int(input("Enter the length of the password:"))

a="".join(random.sample(password, password_length))
print(f"Generated Password is : {a}")