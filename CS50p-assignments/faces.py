# 1. Ask the user for input first
text = input()

# 2. Define the convert function
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text  # CRITICAL: If not done the program will bust. changes the text

# 3. new varriable that can be used to print the result
new = convert(text)
print(new)
