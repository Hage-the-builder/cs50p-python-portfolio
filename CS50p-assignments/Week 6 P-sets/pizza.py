import sys
import os
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    menu = []

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    # The first row contains the headers, and the grid format matches check50 requirements
    print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))

if __name__ == "__main__":
    main()
