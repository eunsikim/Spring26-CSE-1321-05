def main():
    states = {
        "Georgia":"Atlanta", 
        "Florida":"Tallahassee", 
        "Alabama":"Montgomery"
    }

    # This is how we iterate through the keys
    for entry in states:
        print(entry)

    # This is how we iterate through the values
    for entry in states.values():
        print(entry)

    # This is how we iterate through all KV Pair entries
    for entry in states.items():
        print(entry)

    for entry in states.items():
        print(f"State: {entry[0]}, Capital: {entry[1]}")

    # But, if we iterate through the keys, we can
    # ignore the values() and items() functions.
    for entry in states:
        print(states[entry])

    for entry in states:
        print(f"State: {entry}, Capital: {states[entry]}")


if __name__ == "__main__":
    main()