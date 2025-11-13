t = int(input())
for _ in range(t):
    s = input().split()
    for i in s:
        if i.endswith("86"):
            print("YES")
        else:
            print("NO")
