import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User Input
length = int(input("Enter the desired length of the password: "))
password = generate_password(length)

# Display the Password
print("Generated Password:", password)