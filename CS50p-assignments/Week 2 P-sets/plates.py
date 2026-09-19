def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length must be between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: Must start with at least two letters
    if not s[0:2].isalpha():
        return False

    # Rule 3: No periods, spaces, or punctuation allowed
    if not s.isalnum():
        return False

    # Rule 4: Numbers must be at the end, and the first number cannot be '0'
    for i in range(len(s)):
        if s[i].isdigit():
            # If the first number encountered is '0', it's invalid
            if s[i] == '0':
                return False
            # Check if any remaining characters after the first number are letters
            if not s[i:].isdigit():
                return False
            break # if passed all these tests we let it go
    return True


if __name__ == "__main__":
    main()
