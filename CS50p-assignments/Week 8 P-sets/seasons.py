import sys
import re
import inflect
from datetime import date

def main():
    birth_str = input("Date of Birth: ")
    # Explicitly check format using regex as required
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", birth_str):
        sys.exit("Invalid date")

    try:
        # Generate the wording using our standalone single-argument function
        print(convert_to_minutes(birth_str))
    except ValueError:
        sys.exit("Invalid date")


def convert_to_minutes(birth_str):
    p = inflect.engine()

    # Parse the birth date string inside the function
    birth_date = date.fromisoformat(birth_str)
    current_date = date.today()

    # Calculate minutes
    diff = current_date - birth_date
    total_minutes = diff.days * 24 * 60

    # Format words without the grammatical "and"
    words = p.number_to_words(total_minutes, andword="")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
