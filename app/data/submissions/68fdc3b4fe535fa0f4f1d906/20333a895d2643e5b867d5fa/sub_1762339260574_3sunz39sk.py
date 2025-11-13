n = int(input())
for i in range(n):
    m = input().strip()
    if m[0]==m[-1]:
        print("YES")
    else:
        print("NO")