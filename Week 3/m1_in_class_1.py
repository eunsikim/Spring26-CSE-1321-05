def main():
    # 1. Print the prompt, 
    # 2. Read the user input as a String, 
    # 3. Convert the string into a float, 
    # 4. Assign the float value into a variable
    temp_F = float( input("Enter a temperature in F: ") )

    temp_K = (temp_F - 32) * 5 / 9 + 273.15

    print(f"{temp_F} F is {temp_K} K")

if __name__ == "__main__":
    main()