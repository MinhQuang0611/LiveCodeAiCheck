text = str(input())

text = text.title()
text = text.replace("! ", "\n")
text = text.replace("!", "\n")
text = text.replace(".", "")
print(text)