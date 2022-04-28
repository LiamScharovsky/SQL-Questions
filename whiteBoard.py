def getCount(s):
    i = 0
    for letter in s:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            i = i + 1

    return i
print(getCount("hello there fine person"))