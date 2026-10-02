# password strength checker
import re
# password strength checker conditions
# minimum length of 8 characters
# at least one uppercase letter
# at least one lowercase letter
# at least one digit
# at least one special character

def check_password_strength(password):
    if len(password)< 8: #length check
        return "Weak:Password must be at least 8 characters long"

    if not any(char.isdigit() for char in password): #digit check
        return "Weak: Password must contain at least one digit"

    if not any (char. isupper() for char in password): #uppercase check
        return "Weak: Password must contain at least one uppercase letter"

    if not any (char. islower()for char in password): #lowercase check
        return "Weak: Password must contain at least one lowercase letter"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): #special character check
        return "Weak: Password must contain at least one special character"

    return "Strong: Password is strong"

def password_checker():
    print("Welcome to the Password Strength Checker!")
    while True:
        password = input("Please enter your password(or type 'exit' to quit): ")

        if password.lower() == "exit":
            print("Exiting the Password Strength Checker. Goodbye!")
            break

        result = check_password_strength(password)
        print(result)

# Run the password checker tool 
if __name__ == "__main__":
    password_checker()     