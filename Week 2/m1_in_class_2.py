def main():
    cal_consumed = int( input("Enter calories consumed: ") )
    years = int( input("Enter amount of years: ") )

    excess_deficit = cal_consumed - 2500

    pounds_gained_lost = excess_deficit / 3500

    pounds_gained_lost = pounds_gained_lost * 365 * years

    print(f"You have gained/lost {pounds_gained_lost}")

if __name__ == "__main__":
    main()