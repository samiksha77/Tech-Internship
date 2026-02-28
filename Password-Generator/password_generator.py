import random

def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 6): "))
            if length < 6:
                print("Password length must be at least 6.\n")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.\n")


def generate_password(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*"

    all_characters = letters + numbers + symbols
    password = ""

    for i in range(length):
        password += random.choice(all_characters)

    return password


def main():
    print("================================")
    print("      PASSWORD GENERATOR APP     ")
    print("================================\n")

    length = get_password_length()
    password = generate_password(length)

    print("\nPassword generated successfully!")
    print("Your password is:", password)
    print("\nThank you for using the application.")


main()