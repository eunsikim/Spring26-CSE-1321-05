# Assuming:
# - Username: admin
# - Password: 123

# Create a program where the user can login using 
# the login information above.

# The program gives the user 3 tries, 
# if the user fails three times the program terminates.

# If the user successfully login with the correct information, print
# "Login successful"

def main():
    username_data = "admin"
    password_data = "123"

    counter = 3

    while counter > 0:
        username_input = input("Username: ")
        password_input = input("Password: ")

        if username_input == username_data and password_input == password_data:
            print("Login Successful")
            break
        else:
            counter -= 1 # counter = counter - 1
            print(f"Login Incorrect, you have {counter} attempt(s) left")


if __name__ == "__main__":
    main()


