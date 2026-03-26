def main():
    bag = []

    bag.append(50)

    bag.append(50.4)

    bag.append("Apple")

    bag.append(False)

    # The same way we can add any data type in a list
    # we can also add a list inside of another list.
    bag.append([])

    print(bag)

if __name__ == "__main__":
    main()