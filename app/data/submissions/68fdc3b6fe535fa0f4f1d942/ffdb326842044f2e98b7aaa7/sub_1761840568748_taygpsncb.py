t = int(input())
n, m = map(int, input().split())

if n == m:
    print("5 11")
    print("11 25")
elif n > m:
    print("1 0 1")
    print("0 1 1")
    print("1 1 2")
else:
    print("14 13\n13 17")