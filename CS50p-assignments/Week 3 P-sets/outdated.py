def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()

        try:
            # format (MM/DD/YYYY)
            if "/" in date:
                month, day, year = date.split("/")
                # Convert to integer
                month, day, year = int(month), int(day), int(year)

                # Enforce calendar parameters
                if 1 <= month <= 12 and 1 <= day <= 31:
                    break

            #  Word-based format (Month Day, YYYY)
            elif "," in date:
                # Split off the month and day from the year
                month_day, year = date.split(",")
                # Split month string from day string
                month_name, day = month_day.split(" ")

                year = int(year.strip())
                day = int(day)

                # find month number from our list
                if month_name in months:
                    month = months.index(month_name) + 1

                    if 1 <= day <= 31:
                        break
        except (ValueError, IndexError):
            # Catch errors or failed integer conversions
            pass

    # Print in YYYY-MM-DD format
    print(f"{year}-{month:02}-{day:02}")


if __name__ == "__main__":
    main()
