def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
t = int(input())
for _ in range(t):
    s = input().strip()
    ok = True
    for i in range(len(s)):
        if prime(i) != prime(int(s[i])): 
            ok = False
            break
    print("YES" if ok else "NO")