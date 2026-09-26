import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    # 1. First, make sure the string is an actual iframe element
    if re.search(r"<iframe[^>]*>", s):
        # 2. Extract the YouTube ID strictly from a src attribute pointing to embed/
        match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
        if match:
            return f"https://youtu.be/{match.group(1)}"

    return None


if __name__ == "__main__":
    main()
