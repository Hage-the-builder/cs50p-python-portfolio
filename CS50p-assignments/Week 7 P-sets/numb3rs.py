
import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regular expression matching #.#.#.# where each # can be 1-3 digits
    if re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip.strip()):
        parts = ip.split(".")
        for part in parts:
            if not (0 <= int(part) <= 255):
                return False
        return True
    return False


if __name__ == "__main__":
    main()
