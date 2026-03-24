def main():
    grades_list = [80, 90, 30, 55, 100]
    
    # [Iteration by value]
    # We can iterate through a sequence
    # using a for loop
    print("Using a for loop: ")
    for grade in grades_list:
        print(grade)

    # [Iteration by Index]
    # We can iterate through a sequence
    # by accessing elements via index (int) 
    # value
    print("\nUsing a while loop: ")
    counter = 0
    while counter < len(grades_list):
        print(grades_list[counter])
        counter += 1

    print()
    # We can use the len() function to 
    # count how many elements a sequence
    # has.
    # Notice: The number of elements is just
    # the last index + 1
    print(len(grades_list))

if __name__ == "__main__":
    main()