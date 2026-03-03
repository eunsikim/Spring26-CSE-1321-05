def my_formula(number1, number2):
    calc = number1 + number2
    return calc

def my_other_function(x):
    return x * 5


def main():
    # A function call is an expression
    x = my_formula(5, my_other_function(6))

    print(x)

if __name__ == "__main__":
    main()