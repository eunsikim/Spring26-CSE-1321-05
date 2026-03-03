# The return statement is useful for the function
# to communicate with other functions/systems
# but it performs two things:
def my_formula(number1, number2):
    calc = number1 + number2

    # 1. `return` returns a value
    return calc

def is_equal_to_5(x):
    if x == 5:
        return True
    # 2. `return` will stop/break your function
    return False

def helloWorld():
    # If you do not specify a return statement
    # python will return `None`
    # Every function does return a value
    print("Hello World")

def main():
    x = my_formula(5, 6) * 30

    print(x)

    print(is_equal_to_5(5))

    helloWorld()

    print(type(helloWorld()))
    print(type(my_formula(5, 6)))
    print(type(my_formula(5, 6.0)))

if __name__ == "__main__":
    main()