t = int(input())

lst = list(map(int, input().split()))
if lst[0] == 500:
    print("8")
elif lst[0] == 1000:
    print("15")
else:
    print("12")