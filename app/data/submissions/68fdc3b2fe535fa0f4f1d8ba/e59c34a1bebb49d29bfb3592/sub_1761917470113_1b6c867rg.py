n = int(input())
for _ in range(n):
    t = input().strip()
    total = sum(int(ch) for ch in t)
    dk2 = all(abs(int(t[i]) - int(t[i+1])) == 2 for i in range(len(t)-1))
    if total % 10 == 0 and dk2:
        print("YES")
    else:
        print("NO")

