
# 🔐 Random Password Generator
# #Python #PasswordGenerator #RandomPassword #CyberSecurity

import random
import string

# Function to generate a random password
def generate_password(n):
    # Define characters for the password
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"

    password = ""

    # Select random characters to create the password
    for _ in range(n):
        password += random.choice(characters)

    return password


# Main program
if __name__ == "__main__":
    n = 12
    password = generate_password(n)

    print("Randomly generated password:", password)
