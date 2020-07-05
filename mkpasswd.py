        #!/usr/bin/env python

#Select a random set of characters
import random

#Create a list of characters to generate a password from
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

#Ask the user how many passwords they want to generate
number = input("Number of passwords? - ")
number = int(number)

#Ask the user what length in characters the password should be
length = input("Password length? - ")
length = int(length)

for p in range(number):
    password = " "
    for c in range(length):
        password += random.choice(chars)
    print(password)
