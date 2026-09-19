def main():
    while True:
        fuel = input("Fraction: ")
        try:
            # Split the fraction into X and Y strings
            numerator, denominator = fuel.split("/")

            # Convert strings to integers
            x = int(numerator)
            y = int(denominator)

            # Ensure the denominator isn't 0 and X isn't greater than Y
            if x <= y and y != 0 and 0 <= x:
                percentage = round((x / y) * 100)
                break
        except (ValueError, ZeroDivisionError):
            # Catch invalid formatting, non-integers, or dividing by zero
            pass

    # Determine gauge reading
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()
