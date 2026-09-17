# 1. Get the input, remove whitespace, and convert to lowercase
greeting = input("Greeting: ").strip().lower()

# 2. Use an if-elif-else chain to check the rules
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"): # elif means else if or in other words if the rule is found the function will stop here
    print("$20")
else:
    print("$100")
