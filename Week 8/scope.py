def my_formula(number1, number2):
    # The values for number1 and number2
    # are independent from `main()` and they
    # are dependent on the parameter
    print("my_formula:")
    print(number1)
    print(number2)

def main():
    number1 = 10
    number2 = 20
    my_formula(5, 6)
    print()

    # Even though number1 and number2 share the
    # name as in the ones intialized in `my_formula`
    # they refer to different values
    print("main:")
    print(number1)
    print(number2)
    

if __name__ == "__main__":
    main()