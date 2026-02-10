# Challenge: Do not let the program crash if the
# user attemps to do a division by 0.
def main():
    num1 = float(input("Enter number: "))
    op = input("Enter Operation (+, -, *, /): ")
    num2 = float(input("Enter number: "))

    match op:
        case "+":
            res = num1 + num2
        case "-":
            res = num1 - num2
        case "*":
            res = num1 * num2
        case "/":
            res = num1 / num2
    
    print(f"{num1} {op} {num2} = {res}")


if __name__ == "__main__":
    main()
