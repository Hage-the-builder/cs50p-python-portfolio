answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
# 1. Strip whitespace and handle case-insensitivity
answernew = answer.strip().lower()
# have to putt all the ifs together so it only runs the command once.
if answernew == "42" or answernew == "forty two" or answernew == "forty-two":
    print("Yes")

else:
    print("No")
