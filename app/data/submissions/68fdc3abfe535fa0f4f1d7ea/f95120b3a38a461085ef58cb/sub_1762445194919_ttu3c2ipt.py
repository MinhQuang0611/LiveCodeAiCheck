t = int(input())
for _ in range(t):
    n = input().strip()
    numbers = []
    num = ''
    for k in n:
        if k.isdigit():
            num += k
        else:
            if num != '':
                numbers.append(int(num))
                num = ''
    if num != "":
        numbers.append(int(num))
    print(max(numbers))