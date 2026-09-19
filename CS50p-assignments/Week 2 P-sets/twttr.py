def main():
    tweet = input("input: ")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for vowel in vowels:
        tweet = tweet.replace(vowel, "")

    # Print a final newline at the very end
    print(tweet)


if __name__ == "__main__":
    main()
