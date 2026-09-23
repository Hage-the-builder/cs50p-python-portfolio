import random



while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass
                            # sets level and if the level entered is not a number it reasks

secret = random.randint(1, level)
                                        # makes random number

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < secret:
                    print("Too small!")
            elif guess > secret:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass
                                    # the acctual game that tells u if the number you inputted is too large or if its too snall untill you guess it (its not really guessing at this point) if you get it right it stops the code

