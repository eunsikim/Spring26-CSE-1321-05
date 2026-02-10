def main():
    side_num = int(input("Enter sides: "))

    match side_num:
        case 3:
            print("You have a triangle")
        case 4:
            print("You have a quadrilateral")
        case 5:
            print("You have a pentagon")
        case 6:
            print("You have a hexagon")
        case _:
            print("I do not know that shape")

if __name__ == "__main__":
    main()
