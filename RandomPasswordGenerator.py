import random
import string

def generate_random_password(length=12):
    # Define the character sets for different types of characters
    lowercase= string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_-+=<>?/[]{}|'

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure the password length is at least 8 characters
    if length < 8:
        length = 8

    # Generate a random password by selecting characters randomly
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Example usage:
password = generate_random_password()
print("Random Password: ", password)
