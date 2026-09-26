import sys
import os

def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Check file extension
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Check if file exists
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    line_count = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                # Strip leading whitespace to properly detect comments/blank lines
                stripped_line = line.lstrip()
                if stripped_line == "" or stripped_line.startswith("#"):
                    continue
                line_count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(line_count)

if __name__ == "__main__":
    main()
