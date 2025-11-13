a = input()
b = input()
c = input()
if a.lower() == "inf" or b.lower() == "inf" or c.lower() == "inf":
    print("inf")
else:
    a, b, c = int(a), int(b), int(c)
    print(min(a, b, c))