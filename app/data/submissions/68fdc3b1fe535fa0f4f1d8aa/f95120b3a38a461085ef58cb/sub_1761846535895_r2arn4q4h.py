t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split())) 
    b = list(map(int, input().split())) 
    a.sort()
    b.sort()
    can_win = all(a[i] <= b[i] for i in range(n))
    print("YES" if can_win else "NO")