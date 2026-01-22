def main():
    my_number = 10
    print(my_number)
    # We can use `type()` function to check the data type of something
    print(type(my_number))

    my_number = float(my_number)
    print(my_number)
    print(type(my_number))

    my_number = 3.14
    my_number = int(my_number)
    print(my_number)
    print(type(my_number))

    # Conversions between String (str) and Numerical (int, float, etc)
    my_string = "3.14"
    my_string = float(my_string)
    print(my_string)

if __name__ == "__main__":
    main()