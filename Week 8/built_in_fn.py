def my_formula(number1, number2, number3 = 5, number4 = 1):
    calc = number1 + number2 * number3 * number4
    return calc

def main():
    print("Hello", end=", ")
    print("World")
    # input("Enter your name:\n")
    print(my_formula(5, 6, 30))

    message = "Hello World".upper()
    print(message)

    # message.capitalize() #Hello world
    message = message.capitalize()
    print(message)

if __name__ == "__main__":
    main()