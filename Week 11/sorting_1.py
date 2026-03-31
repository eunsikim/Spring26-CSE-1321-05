# Bubble Sort
def main():
    my_numbers = [33, 46, 15, 1, 24]

    print(my_numbers)

    iteration_counter = 1

    sub_iteration_counter = 1

    for i in range(len(my_numbers)):
        for j in range(len(my_numbers) - i - 1):
            if my_numbers[j] > my_numbers[j + 1]:
                my_numbers[j], my_numbers[j + 1] = (my_numbers[j + 1], my_numbers[j])
            sub_iteration_counter += 1
        iteration_counter += 1
    
    print(my_numbers)

    print(f"It took me {iteration_counter} iterations (outer loop), and {sub_iteration_counter} sub iterations (inner loop).")

if __name__ == "__main__":
    main()