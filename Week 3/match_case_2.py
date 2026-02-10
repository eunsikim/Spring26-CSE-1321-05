def main():
    x = 10

    if x < 11:
        print("x is less than 11")
    else:
        print("x is greater than or equal to 11")

    # Do the code above but using a single `MATCH` statement.
    # `x` can be [-inf, inf]
    # You cannot use `IF`  
    match x < 11:
        case True:
            print("x is less than 11")
        case False:
            print("x is greater than or equal to 11")
    
    # Challenge: What if we add an `ELIF` statement
    # You can use multiple `MATCH` statement, but nested

if __name__ == "__main__":
    main()
