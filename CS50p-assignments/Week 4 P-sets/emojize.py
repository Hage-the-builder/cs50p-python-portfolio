import emoji

# 1. ask user for what he wants to convert
premoji = input("Input: ")

# 2. Convert text using language='alias' to support both types of codes
aftermoji = emoji.emojize(premoji, language='alias')

# 3. Print the results prefixed with "Output: "
print(f"Output: {aftermoji}")

