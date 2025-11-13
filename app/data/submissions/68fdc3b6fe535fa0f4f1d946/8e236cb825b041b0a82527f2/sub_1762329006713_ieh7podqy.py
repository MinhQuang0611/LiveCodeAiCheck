s = input()
words = []
word = []
for c in s:
    if c.isalnum() or c == ":" or c == ",":
        word.append(c)
    elif c == " ":
        w = "".join(word).lower().capitalize()
        if not w.isspace() and w != "":
            words.append(w)
        word.clear()

w = "".join(word).lower().capitalize()
if not w.isspace() and w != "":
    words.append(w)

print(" ".join(words))