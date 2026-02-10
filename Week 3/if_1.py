def main():
    # Checks a phone battery and prints if it is
    # Fully Charged or not

    phone_battery = 50

    if phone_battery == 100:
        print("Your phone is fully charged")
    elif phone_battery >= 50:
        print("Your phone has at least half charge")
    elif phone_battery >= 30:
        print("You should charge your phone")
    else:
        print("Your phone is not fully charged")

if __name__ == "__main__":
    main()