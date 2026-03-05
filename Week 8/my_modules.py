def is_even(number):
    if number % 2 == 0:
        return True
    return False

def is_equal_to_10(number):
    return number == 10

def what_is_name():
    print(__name__)

def main():
    print("Hello World")
    what_is_name()

if __name__ == "__main__":
    main()