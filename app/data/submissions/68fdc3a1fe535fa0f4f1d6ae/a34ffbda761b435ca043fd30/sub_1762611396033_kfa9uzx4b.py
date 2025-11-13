a = int(input())
for i in range(a):
    n = input()
    while int(n) % 7 != 0:
        n = int(n) + int(str(n)[::-1])
    print(n)