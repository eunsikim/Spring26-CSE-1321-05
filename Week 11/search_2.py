# Binary Search
def main():
    my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    target = 1

    counter = 1

    found = False

    low_index = 0
    high_index = len(my_numbers) - 1
    middle_index = int((high_index - low_index) / 2)

    while low_index < high_index:
        if my_numbers[middle_index] == target:
            found = True
            break
        elif my_numbers[middle_index] > target:
            high_index = middle_index
            middle_index = int((high_index - low_index) / 2)
            counter += 1
        elif my_numbers[middle_index] < target:
            low_index = middle_index
            middle_index = int((high_index - low_index) / 2) + middle_index
            counter += 1
    
    if found == True:
        print(f"We have found {target} in the list")
        print(f"It took me {counter} repetitions to find it!")
    else:
        print(f"We have not found {target} in the list")


if __name__ == "__main__":
    main()