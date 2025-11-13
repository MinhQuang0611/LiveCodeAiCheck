t = int(input())
for _ in range(t):
    s = input()
    is_valid = True
    for ch in s:
        if ch != '4' and ch != '7':
            is_valid = False
            break
    print("YES" if is_valid else "NO")