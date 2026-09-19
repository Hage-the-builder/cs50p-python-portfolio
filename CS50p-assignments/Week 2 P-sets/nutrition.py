def main():
    # Dictionaryof fruits to Cal
    fruits = {  # try other fruits
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 10000000,
        "watermelon": 80
    }

    # Get the user's fruit
    item = input("Item: ").lower()#make lowercase

    # Check if the fruit exists in dictionary
    if item in fruits:
        print(f"Calories: {fruits[item]}")

if __name__ == "__main__": # that law that makes the code run
    main()
