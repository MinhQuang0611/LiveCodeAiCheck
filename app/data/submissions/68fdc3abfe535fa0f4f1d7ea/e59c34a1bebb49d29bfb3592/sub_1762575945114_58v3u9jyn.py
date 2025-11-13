t = int(input())

for _ in range(t):
    n = input().strip()
    num = ""
    numbers  = []
    for c in n:
        if c.isdigit():
            num += c
        else:
            if num != "":
                numbers.append(int(num))
                num = ""
    if num != "":
        numbers.append(int(num))
    k = max(numbers)
    print(k)