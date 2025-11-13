n = int(input())
for i in range(n):
    m = input()
    if m[0] == m[len(m) - 1]:
        print("YES")
    else:
        print("NO")