def main():
    grocery_list = {}

    while True:
        try:
            # make uppercase
            item = input().upper()

            # puts items in list
        
            if item in grocery_list:
                grocery_list[item] += 1
            else:                           # makes one of every item
                grocery_list[item] = 1

        except EOFError:
            print()
            # makes list alphabetical order
            for item in sorted(grocery_list.keys()):
                print(f"{grocery_list[item]} {item}")
            break


if __name__ == "__main__":
    main()
