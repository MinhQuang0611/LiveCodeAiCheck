t = int(input())  # Số lượng test case

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))

    hop_le = all(a[i] <= b[i] for i in range(n))
    print("YES" if hop_le else "NO")
