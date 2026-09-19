def main():
    amount_due = 50

    # Loop until the user has inserted enough coins
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        # Check if the coin is an accepted
        if coin in [25, 10, 5]:
            amount_due -= coin

    # Calculate change owed (making it absolute value to make the change positive)
    print(f"Change Owed: {abs(amount_due)}")

if __name__ == "__main__":
    main()
