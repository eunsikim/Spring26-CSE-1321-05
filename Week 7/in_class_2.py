# Create a function called `isDivisible` that takes in 2 numbers as parameter
# then checks if the first number is disible by the second.
# If they are divisible, the function should print that they are and if not
# the function should return False.

# Add function below this line...
def isDivisible(num1, num2):
    if num1 % num2 == 0:
        print(f"{num1} is divisible by {num2}")
    else:
        return False

def main():
    num1 = 3
    num2 = 6

    if isDivisible(num1, num2) == False:
        print(f"{num1} is not divisible by {num2}")

if __name__ == "__main__":
    main()
    