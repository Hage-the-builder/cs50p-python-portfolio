import random


def main():
    level = get_level()
    score = 0
                    #definitons

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        tries = 0
                            #makes 10 problems

        while tries < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                    print("EEE")
                    tries += 1
                                    #the acctual game, when you answer correctly it will give a point to the score and when not it will tally a "try" and say EEE

        if tries == 3:
            print(f"{x} + {y} = {correct_answer}")
                                                    # when trys exeed 3 it will give the answer
    print(f"Score: {score}")
                                #at the end it will print the score

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

                                        #here it genarates the numbers in the questions

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
                                        #here it asks the player for a level and if it is not 1 , 2 ,or 3 it will ask again

if __name__ == "__main__":
    main()
