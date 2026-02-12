def main():
    # Whenever we use `range()` with a single integer (n),
    # We start from 0 INCLUSIVE and n EXCLUSIVE (n-1 INCLUSIVE)
    for x in range(11):
        print(f"x = {x}")

    # Whenever we use `range()` with a two integer (n, m),
    # We start from n INCLUSIVE and m EXCLUSIVE (m-1 INCLUSIVE)
    for x in range(5, 11):
        print(f"x = {x}")

    # Whenever we use `range()` with a three integer (n, m, o),
    # We start from n INCLUSIVE and m EXCLUSIVE (m-1 INCLUSIVE)
    # and jump `o` times from one number to another
    for x in range(0, 51, 10):
        print(f"x = {x}")
    
    for x in range(50, -1, -10):
        print(f"x = {x}")

    for x in range(0, -51, -10):
        print(f"x = {x}")
        

    

if __name__ == "__main__":
    main()