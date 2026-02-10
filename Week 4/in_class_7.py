def main():
    subtotal = float(input("What is the subtotal: $"))

    if subtotal > 100:
        print(f"Total: ${subtotal - 20}")
    elif subtotal > 50:
        print(f"Total: ${subtotal - 5}")
    else:
        print(f"Total: ${subtotal}")

if __name__ == "__main__":
    main()