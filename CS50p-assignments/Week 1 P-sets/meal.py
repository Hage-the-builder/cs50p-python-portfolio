def main():

    time_input = input("What time is it? ").strip()


    time_float = convert(time_input)


    if 7.0 <= time_float <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_float <= 13.0:
        print("lunch time")
    elif 18.0 <= time_float <= 19.0:
        print("dinner time")

def convert(time):

    hours, minutes = time.split(":")


    if "p.m." in minutes:
        minutes = minutes.replace("p.m.", "").strip()

        if int(hours) != 12:
            hours = int(hours) + 12
    elif "a.m." in minutes:
        minutes = minutes.replace("a.m.", "").strip()

        if int(hours) == 12:
            hours = 0


    return float(hours) + (float(minutes) / 60.0)


if __name__ == "__main__":
    main()
