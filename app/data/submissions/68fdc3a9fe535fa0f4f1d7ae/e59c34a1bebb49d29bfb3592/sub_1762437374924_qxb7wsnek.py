n = int(input())
numbers = []
for _ in range(n):
    t = input().strip()
    num = ""
    for c in t:
        if c.isdigit():
            num += c
        else:
            if num != "":
                numbers.append(int(num))
                num = ""
    if num != "":
        numbers.append(int(num))
numbers.sort()
for x in numbers:
    print(x)