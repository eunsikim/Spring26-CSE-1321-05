def average(*grades):
    sum_grades = 0

    for grade in grades:
        sum_grades += grade

    return sum_grades / len(grades)

def main():
    print(average(50, 44, 30, 100, 98))

if __name__ == "__main__":
    main()