def main():
    age = int(input("Enter your age: "))

    if age < 12:
        print("Ticket Total: $8")
    elif age >= 65:
        print("Ticket Total: $10")
    else: # Implicit expression: age >= 12 and age < 65
        print(f"Ticket Total: $15")

if __name__ == "__main__":
    main()