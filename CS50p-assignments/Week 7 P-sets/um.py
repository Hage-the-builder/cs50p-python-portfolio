import re

def main():
    print(count(input("Text: ")))


def count(s):
    # Using \b word boundaries to match "um" as an independent token cleanly
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
