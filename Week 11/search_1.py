# Linear Search
# Iterate through each item in a list, check if the item
# is the target you are looking for.
def main():
    # my_numbers = [56, 29, 51, 40, 91, 18, 26, 66, 90, 30, 94, 28, 2, 38, 4, 47, 12, 35, 25, 52, 63, 92, 15, 60, 14, 34, 59, 74, 73, 88, 61, 67, 82, 71, 65, 21, 43, 62, 55, 89, 93, 33, 16, 31, 77, 10, 5, 78, 84, 85, 19, 8, 97, 37, 32, 96, 44, 9, 6, 46, 49, 45, 68, 17, 72, 13, 24, 3, 36, 75, 1, 20, 76, 7, 39, 23, 57, 70, 41, 58, 11, 81, 54, 22, 48, 100, 87, 98, 80, 79, 83, 50, 27, 69, 95, 86, 99, 64, 53, 42, 150]
    my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    target = 1

    counter = 1

    found = False

    for number in my_numbers:
        if number == target:
            found = True
            break
        else:
            counter += 1

    if found == True:
        print(f"We have found {target} in the list")
        print(f"It took me {counter} repetitions to find it!")
    else:
        print(f"We have not found {target} in the list")

if __name__ == "__main__":
    main()