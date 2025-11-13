t = int(input())
for _ in range(t):
    n = input()
    a = []
    for i in range(len(n)):
        if n[i].isalpha():
            a.append(' ')
        if n[i].isdigit():
            a.append(n[i])
    a = ''.join(a).split()
    for x in a:
        x = int(x)
    print(min(a))
                    