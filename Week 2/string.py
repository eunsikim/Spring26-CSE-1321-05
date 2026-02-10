def main():
    # Strings are immutable
    text = "Hello World"

    print(text)
    print(len(text)) # Use the `len()` function to find out how many characters in `text`

    text = "Hello CSE 1321"

    print(text)
    print(len(text))

    # Escape Sequences
    # For String actions/Characters
    my_string = "\"This is a text\nThis is the continuation of the text\""
    print(my_string)



if __name__ == "__main__":
    main()