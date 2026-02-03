def main():
    age = int(input("Enter your age: "))
    isAfter4 = input("Is the screening after 4 PM (Y/N): ")

    ticketPrice = 0

    if age < 12 and isAfter4 == "Y":
        ticketPrice = 8
    elif age < 12: # and isAfter4 == "N"
        ticketPrice = 6
    elif age >= 65 and isAfter4 == "Y":
        ticketPrice = 10
    elif age >= 65: # and isAfter4 == "N"
        ticketPrice = 8
    elif isAfter4 == "Y": # and (age >= 12 and age < 65)
        ticketPrice = 15
    else: # isAfter4 == "N" and (age >= 12 and age < 65)
        ticketPrice = 13

    print(f"Ticket Price: ${ticketPrice}")

if __name__ == "__main__":
    main()