def main():
    counter = 1
    for x in range(10):
        for y in range(10):
            for z in range(10):
                print(f"{counter}: Hello World")
                counter += 1


if __name__ == "__main__":
    main()
