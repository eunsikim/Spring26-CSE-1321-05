def main():
    menuOrder = input("What do you want to order: ")

    match menuOrder:
        case "burger":
            print("You ordered a burger")
        case "fries":
            print("You ordered fries")
        case "drink":
            print("You ordered a drink")
        case _:
            print("We do not have that.")
        
    
    print("...Resuming program...")

if __name__ == "__main__":
    main()
