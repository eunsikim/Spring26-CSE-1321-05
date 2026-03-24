def main():
    # Initialize an empty list
    grades = []
    # Initialize a list with initial value(s)
    names = ["John", "Dave"]

    # We can output a list with a print statement
    print(names)

    # Append will add the new element at the end of the list
    # (the next available position/index)
    print(f"Grades list: {grades}")
    grades.append(80)
    print(f"Grades list: {grades}")
    grades.append(90)
    print(f"Grades list: {grades}")
    grades.append(30)
    print(f"Grades list: {grades}")

    # Insert will add the new element at the specified index*
    # *Only if the index value is the next available index or 
    # an index already filled in.
    grades.insert(3, 50)
    print(f"Grades list: {grades}")
    grades.insert(3, 55)
    print(f"Grades list: {grades}")

    # We can modify an element in a list by using its index
    # That index must exist
    grades[4] = 100
    print(f"Grades list: {grades}")

    # We can use the del keyword to delete an element in a
    # specific index
    del grades[4]
    print(f"Grades list: {grades}")

    # Similar to `del`, but this function will also return
    # the removed element after removing it from the list
    print(f"Deleting record on index 1: {grades.pop(1)}")
    print(f"Grades list: {grades}")

    grades.append(30)
    print(f"Grades list: {grades}")

    # This function will remove the first occurrence of the
    # value passed as argument
    grades.remove(30)
    print(f"Grades list: {grades}")
    grades.remove(30)
    print(f"Grades list: {grades}")

    grades.clear()
    print(f"Grades list: {grades}")





if __name__ == "__main__":
    main()