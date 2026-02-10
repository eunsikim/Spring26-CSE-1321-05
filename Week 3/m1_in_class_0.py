def main():
    # 1. Print the prompt, 
    # 2. Read the user input as a String, 
    # 3. Convert the string into a float, 
    # 4. Assign the float value into a variable
    earth_weight = float( input("Enter your earth weight: ") )

    moon_weight = (16.5 / 100) * earth_weight

    print(f"Your moon weight is: {moon_weight}")

if __name__ == "__main__":
    main()