def main():
    counter = 0

    while True:
        if counter == 50:
            break
        elif counter % 2 == 0:
            counter += 1
            # If the program executes a `continue`
            # it will jump into the NEXT iteration
            continue

        print(f"counter: {counter}")

        counter += 1
        
if __name__ == "__main__":
    main()
