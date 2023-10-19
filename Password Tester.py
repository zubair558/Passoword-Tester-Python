import re


def is_strong_password(password):
    # Check if password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if password contains both uppercase and lowercase letters
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return False

    # Check if password contains at least one digit
    if not re.search("[0-9]", password):
        return False

    # Check if password contains at least one special character
    special_characters = "!@#$%^&*()_+[]{}|;:,.<>?/"
    if not any(char in special_characters for char in password):
        return False

    return True


def get_password_from_user():
    while True:
        password = input("Enter your password: ")
        if is_strong_password(password):
            print("Strong password! Good job!")
            break
        else:
            print("Weak password! Please choose a stronger one.")
            print(
                "Password must be at least 8 characters long and include uppercase letters, lowercase letters, digits, and special characters.")


# Main function
def main():
    print("Welcome to the Password Tester!")
    get_password_from_user()


if __name__ == "__main__":
    main()
