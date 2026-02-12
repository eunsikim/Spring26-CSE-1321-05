# Password Validator
# Create a program that accepts a password and validates it (If it is valid or not)

# Password Rules:
# - The password must contain AT LEAST one number
# - The password must have 8 characters or more
# - The password must not be larger than 16 characters
# - If the user fails (invalid password), re-prompt the user for another one

# HINT:
# - Remember we can iterate through each character in a string using a FOR loop

def main():
    password = input("Enter your password: ")

    hasNumber = False

    for c in password:
        if c == "0" or c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9":
            hasNumber = True
            break

    if hasNumber == True:
        print("Valid Password")
    else:
        print("Invalid Password")  

if __name__ == "__main__":
    main()