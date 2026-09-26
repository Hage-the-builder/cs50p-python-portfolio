import validators

def main():
    email = input("What's your email address? ").strip()

    # Uses the validators package to handle production grade validation parameters
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
