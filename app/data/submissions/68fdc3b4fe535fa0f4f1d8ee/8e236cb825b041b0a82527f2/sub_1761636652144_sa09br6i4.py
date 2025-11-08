t = int(input())
for _ in range(t):
    for c in input():
        if c != "4" and c != "7":
            print("NO")
            break
    else:
        print("YES")