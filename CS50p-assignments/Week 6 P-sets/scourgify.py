import sys
import os
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        sys.exit(f"Could not read {input_file}")

    cleaned_data = []

    try:
        with open(input_file, "r") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                # Split "Last, First" by the comma
                last, first = row["name"].split(", ")
                cleaned_data.append({
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": row["house"]
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    # Write the formatted information to the output file
    with open(output_file, "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(cleaned_data)

if __name__ == "__main__":
    main()
