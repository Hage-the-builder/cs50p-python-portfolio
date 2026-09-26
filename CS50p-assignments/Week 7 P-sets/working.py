import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regex targeting: Hour(:Minute)? (AM|PM) to Hour(:Minute)? (AM|PM)
    pattern = r"^([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM) to ([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM)$"
    match = re.search(pattern, s.strip())

    if not match:
        raise ValueError

    hr1, min1, period1, hr2, min2, period2 = match.groups()

    # Defaults minutes to 00 if omitted
    min1 = min1 if min1 else "00"
    min2 = min2 if min2 else "00"

    # Enforce standard clocks boundaries
    if not (1 <= int(hr1) <= 12) or not (1 <= int(hr2) <= 12):
        raise ValueError

    # Normalize AM/PM adjustments
    def to_24(hr, period):
        hr = int(hr)
        if period == "AM":
            return 0 if hr == 12 else hr
        else: # PM
            return 12 if hr == 12 else hr + 12

    return f"{to_24(hr1, period1):02}:{min1} to {to_24(hr2, period2):02}:{min2}"


if __name__ == "__main__":
    main()
