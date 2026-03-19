import random

def main():
    random.seed(10)

    print("This is using `randint(5, 10)")
    for i in range(10):
        num_1 = random.randint(5, 10)
        
        print(num_1)

    print("\nThis using `randrange(5, 10)`")
    for i in range(10):
        num_2 = random.randrange(5, 11)

        print(num_2)

if __name__ == "__main__":
    main()