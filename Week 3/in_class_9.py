def main():
    subtotal = float(input("Enter a subtotal: "))
    isMember = input("Are you a member (Y/N): ") == "Y"

    if isMember == True or subtotal >= 75:
        shippingFee = 0
    else:
        shippingFee = 10
    
    total = subtotal + shippingFee

    print(f"Subtotal: ${subtotal}")
    print(f"Shipping Fee: ${shippingFee}")
    print(f"Total: ${total}")

if __name__ == "__main__":
    main()