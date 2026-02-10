def main():
    x = 1

    print(f"`x` has been initalized with the value of {x}\n")

    while x <= 3:
        print("Hello World")
        print("-----------")

        x += 1
    
    print()
    print(f"`x` stopped at the value of {x}")

if __name__ == "__main__":
    main()