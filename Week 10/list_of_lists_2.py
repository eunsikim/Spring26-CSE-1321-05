def main():
    # `students` is a list that contains the name of a student
    # and their grades for 7 Quiz grades
    students = [
                ["John", 84.3, 78.65, 50, 40, 50, 67, 89], 
                ["Abigail", 89.5, 78.65, 50, 40, 50, 67, 89],
                ["David", 60, 78.65, 50, 40, 50, 67, 89],
                ["Steve", 85, 78.65, 50, 40, 50, 67, 89],
                ["Sam", 54.2, 78.65, 50, 40, 50, 67, 89],
               ]

    # print(f"{students[0][0]} {students[0][1]}")
    # print(f"{students[1][0]} {students[1][1]}")
    # print(f"{students[2][0]} {students[2][1]}")
    # print(f"{students[3][0]} {students[3][1]}")
    # print(f"{students[4][0]} {students[4][1]}")

    sublist_index = 0

    while sublist_index < len(students):
        data_index = 0
        while data_index < len(students[0]):
            print(students[sublist_index][data_index], end=" ")
            data_index += 1
        print()
        sublist_index += 1



if __name__ == "__main__":
    main()