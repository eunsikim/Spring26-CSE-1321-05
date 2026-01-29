def main():
    valid_username = "ADMIN"
    valid_password = "123"

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == valid_username and password == valid_password:
        print("You have successfully logged in")
    else:
        print("Loggin information incorrect")

    if password != valid_password:
            print("Incorrect password")
    elif username != valid_username:
        print("Incorrect username")

if __name__ == "__main__":
    main()