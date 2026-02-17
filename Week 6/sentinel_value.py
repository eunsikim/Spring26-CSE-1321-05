# Challenge: Do not let the program crash if the
# user attemps to do a division by 0.
def main():
    # We initalize `restart` with a value of "Y"
    # to ensure we execute the while the first try.
    restart = "Y"

    while restart == "Y":
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

        while True:
            # SENTINEL VALUE: 'Y' to continue and 'N' to stop
            restart = input("Another calculation? (Y/N): ")

            if restart != "Y" and restart != "N":
                print("Please enter 'Y' for yes or 'N' for no")
            else:
                break
        


if __name__ == "__main__":
    main()
