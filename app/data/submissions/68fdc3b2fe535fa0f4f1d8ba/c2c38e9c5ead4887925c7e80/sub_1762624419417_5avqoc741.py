t = int(input())

for _ in range(t):
    s = input()
    tong = sum(int(c) for c in s)
    hop_le = tong % 10 == 0

    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i + 1])) != 2:
            hop_le = False
            break

    print("YES" if hop_le else "NO")
