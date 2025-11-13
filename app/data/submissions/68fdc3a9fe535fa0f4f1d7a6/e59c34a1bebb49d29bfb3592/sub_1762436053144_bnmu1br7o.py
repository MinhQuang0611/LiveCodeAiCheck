t = int(input())
for _ in range(t):
    n = input()
    numbers = []
    num = ''
    for c in n:
        if c.isdigit():
            num += c
        else:
            if num != '':
                numbers.append(int(num))
                num = ''
    if num != "":
        numbers.append(int(num))
    print(min(numbers))