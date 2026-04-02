def main():
    my_list = [9, 8, 1]
    # Key-Value Pair (KV Pair)
    my_dictionary = {
        "Hello":"World",
        3.14:"pi",
        "pi":3.14
    }

    print(my_list[1])
    print(my_dictionary["Hello"])
    print(my_dictionary[3.14])
    print(my_dictionary["pi"])

    print(my_dictionary)

    # Python checks if the key exist within the
    # the dictionary.
    # If it doesnt exist, it will add a new KV Pair
    my_dictionary["CSE 1321"] = "05"
    print(my_dictionary)

    # If the key exists, python will modify a KV Pair
    my_dictionary["CSE 1321"] = "51"
    print(my_dictionary)

    # We can delete a KV Pair using the pop function
    # which returns the deleted KV Pair value
    print(my_dictionary.pop("Hello"))

    print(my_dictionary)

    # We can also use the `del` statement
    del my_dictionary["CSE 1321"]   

    print(my_dictionary)

    # And clear or empty the dictionary
    my_dictionary.clear()

    print(my_dictionary)




if __name__ == "__main__":
    main()