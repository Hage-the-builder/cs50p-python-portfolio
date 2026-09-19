def main():
    # ask for user for input
    camel_case = input("camelCase: ")

    print("snake_case: ", end="")

    # goes through each letter
    for char in camel_case:
        # If the character is uppercase, will print a _ then the lower case
        if char.isupper():
            print("_" + char.lower(), end="")
        else:
            print(char, end="")

    # Print a new line at the end or it will look like this: h_imy_nameWeek-2/Camelcase/ $ python camel.py
    print()

if __name__ == "__main__":
       main()
