def main():
    age = int(input("Enter your age: "))
    isAfter4 = input("Is the screening after 4 PM (Y/N): ")

    ticketPrice = 0

    if age < 12:
        ticketPrice = 8

        if isAfter4 == "N":
            ticketPrice -= 2 # ticketPrice = ticketPrice - 2
    elif age >= 65:
        ticketPrice = 10

        if isAfter4 == "N":
            ticketPrice -= 2
    else:
        ticketPrice = 15

        if isAfter4 == "N":
            ticketPrice -= 2

    print(f"Ticket Price: ${ticketPrice}")

if __name__ == "__main__":
    main()