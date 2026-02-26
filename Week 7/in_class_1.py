# Create a function called `isEven` that takes in 
# one number as parameter and return True
# if the parameter is even or False if the parameter
# is odd.

# INPUT: 1 numeric parameter
# PROCESS: Check if the parameter is even
# OUTPUT: True if the parameter is even, False if it is odd
def isEven(num):
    if num % 2 == 0: # EVEN
        # `return` will return the value of `True`
        # but also STOP/BREAK the function
        return True 
    else:
        return False

def main():
    if isEven(33):
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
    main()