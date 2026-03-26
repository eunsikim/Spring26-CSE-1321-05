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

    for sublist in students:
        for data in sublist:
            print(data, end = " ")
        print()



if __name__ == "__main__":
    main()