import sys
import inflect
                # import needed packages

p = inflect.engine()
                    # have to have this so a typeerror does not appeer





names = []
                # have to define the list even though it is empty as you fill ask the user to fill it




while True:
    try:
        name = input("Name: ")
        names.append(name)
                                        # ask user for the names add them to the list



    except EOFError:
        print()
        break
                                # when the user is done and presses controll d to get kicked out of the naming loop


listednames = p.join(names)
print(f"Adieu, adieu, to {listednames}")
                                            # make the list in the meant order and print

