def main():
    my_tuple = (3, 9, 5, 10)

    print(my_tuple)

    my_tuple = list(my_tuple)

    print(my_tuple)

    my_tuple.append(55)

    print(my_tuple)

    my_tuple = tuple(my_tuple)
    
    print(my_tuple)

if __name__ == "__main__":
    main()