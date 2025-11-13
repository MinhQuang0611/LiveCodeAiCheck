n =int(input())
for i in range(n):
    t = input()
    if t == t[::-1]:
        print("YES")
    else:
        print("NO")