t = int(input())

while t > 0:
    n = int(input())

    team_a = list(map(int, input().split()))
    team_b = list(map(int, input().split()))

    check = True

    for i in range(n):
        if team_a[i] > team_b[i]:
            check = False

    if check:
        print("YES")
    else:
        print("NO")
    t -= 1