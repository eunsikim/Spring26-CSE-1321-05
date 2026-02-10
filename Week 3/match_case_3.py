def main():
    menuOrder = 10.0

    match menuOrder:
        case "burger":
            print("You ordered a burger")
        case "fries":
            print("You ordered fries")
        case "drink":
            print("You ordered a drink")
        case "10":
            print("We do not sell strings")
        case 10.0:
            print("We do not sell floats")
        case 10:
            print("We do not sell integers")
        
        case _:
            print("We do not have that.")
        
    
    print("...Resuming program...")

if __name__ == "__main__":
    main()
