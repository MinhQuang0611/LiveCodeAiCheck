text = input()
words = text.split()
result = []

for word in words:
    result.append(word.capitalize())

print(" ".join(result))