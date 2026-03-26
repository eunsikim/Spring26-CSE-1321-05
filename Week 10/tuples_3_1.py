def get_user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    user_info = (name, age)

    return user_info

def main():
    name, age = get_user_info()

    print(f"Hello {name}, you are {age} years old.")

if __name__ == "__main__":
    main()