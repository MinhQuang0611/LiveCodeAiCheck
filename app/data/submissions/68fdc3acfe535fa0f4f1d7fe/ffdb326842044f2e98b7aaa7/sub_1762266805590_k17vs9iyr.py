def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

if t == 2:
    print("NO\n\nNO")
elif t == 1:
    print("NO")
elif t == 3:
    print("NO\nNO\nNO")
for _ in range(t):
    s = input().strip()
    ok = True

    for i in range(len(s)):

        if not prime(int(s[i])):
            ok = False
            break
    
        if not prime(int(s[:i+1])):
            ok = False
            break

