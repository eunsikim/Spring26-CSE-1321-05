# number1 and number2 are Required params
# number3 is an Optional params
def my_formula(number1, number2, number3 = 5):
    calc = number1 + number2 * number3
    return calc

def my_other_function(number1 = 5):
    print(number1)

def main():
    x = my_formula(5, 6)

    print(my_formula("3", "5", 3))

    print(x)

    print(my_formula(5, 6, 2))

    my_other_function()
    my_other_function(100)

if __name__ == "__main__":
    main()