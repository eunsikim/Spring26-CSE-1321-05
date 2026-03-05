import my_modules

def main():
    print(my_modules.is_even(100))
    print(my_modules.is_equal_to_10(5))
    my_modules.what_is_name()
    print(__name__)

if __name__ == "__main__":
    main()