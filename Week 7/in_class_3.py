# `x` is global, is visible throughout the different functions
x = 10
def function_1(num1):
    x = 100
    # Even though we have `num1` defined in the `main()`
    # `num1` in `function_1()` is different
    print(num1) 
    print(num2) # num2 is only "visible" within `main()`
    print(x)
    
def main():
    # num1 and num2 are local to `main()`, they only exist
    # and are visible inside the `main()`.
    num1 = 3
    num2 = 6

    print(num1)
    function_1(num2)
    print(x)


if __name__ == "__main__":
    main()
    