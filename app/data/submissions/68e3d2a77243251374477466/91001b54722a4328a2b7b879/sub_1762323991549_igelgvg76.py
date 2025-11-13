s = input()
words = s.split()
result = " ".join(word[::-1] for word in words)
print(result)