import random
import string

def generate_password(length):
    dictionary = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(dictionary, length))
    return password

def get_length():
    length = int(input("Enter the length of password : "))
    return length

print(generate_password(get_length()))