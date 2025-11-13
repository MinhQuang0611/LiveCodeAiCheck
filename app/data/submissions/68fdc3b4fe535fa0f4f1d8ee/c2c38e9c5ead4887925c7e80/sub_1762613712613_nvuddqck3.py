t = int(input())
for _ in range(t):
    n = input()
    if all(ch in '47' for ch in n):
        print("YES")
    else:
        print("NO")
