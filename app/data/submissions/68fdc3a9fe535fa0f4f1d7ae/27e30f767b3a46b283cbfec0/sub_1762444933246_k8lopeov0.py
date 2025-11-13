n = int(input())
numbers = []
for _ in range(n):
    s = input()
    num = ''
    for ch in s:
        if ch.isdigit():
            num += ch
        else:
            if num != '':
                numbers.append(int(num))
                num = ''
    if num != '':
        numbers.append(int(num))

numbers.sort()

for x in numbers:
    print(x)
