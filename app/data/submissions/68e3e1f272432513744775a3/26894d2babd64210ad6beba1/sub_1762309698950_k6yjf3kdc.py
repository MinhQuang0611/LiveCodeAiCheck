a = input()
b = input()
c = input()

if a == b == c == "inf":
    print("inf")
else:
    print(min(int(a), min(int(a), int(c ))))