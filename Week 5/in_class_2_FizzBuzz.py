# Challenge: Let the user decide the length sequence
def main():
    counter = 1

    while counter <= 15:
        if counter % 3 == 0 and counter % 5 == 0:
            print("FizzBuzz")
        elif counter % 3 == 0:
            print("Fizz")
        elif counter % 5 == 0:
            print("Buzz")
        else:
            print(counter)

        counter += 1

if __name__ == "__main__":
    main()