def main():
    variable = 10 < 5

    match variable:
        case 0:
            print("This is an boolean")
        case int():
            print("This is an int")
        case float():
            print("This is an float")
        case str():
            print("This is an string")

if __name__ == "__main__":
    main()
