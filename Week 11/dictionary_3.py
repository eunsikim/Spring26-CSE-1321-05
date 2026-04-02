def exists(value, dictionary):
    if value in dictionary:
        print(f"{value} exists!")
    else:
        print(f"{value} does not exists!")

def main():
    states = {
        "Georgia":"Atlanta", 
        "Florida":"Tallahassee", 
        "Alabama":"Montgomery"
    }

    for state in states:
        if states[state] == "Atlanta":
            print("Atlanta exists!")

    exists("Atlanta", states)
    exists("Atlanta", states.values())
    exists(("Alabama", "Tallahassee"), states.items())
    exists(("Florida", "Tallahassee"), states.items())

if __name__ == "__main__":
    main()