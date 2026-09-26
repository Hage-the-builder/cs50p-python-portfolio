def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(percentage))


def convert(fraction):
    if "/" not in fraction:
        raise ValueError

    numerator, denominator = fraction.split("/")
    if not numerator.isdigit() or not denominator.isdigit():
        raise ValueError

    x, y = int(numerator), int(denominator)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
