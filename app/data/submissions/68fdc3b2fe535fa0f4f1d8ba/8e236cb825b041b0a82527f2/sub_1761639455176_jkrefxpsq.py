def is_valid(n):
    if n % 2 != 0:
        return False
    
    ss = 0
    prev = -1
    while n > 0:
        d = n % 10
        if prev != -1 and abs(prev - d) != 2:
            return False
        
        prev = d
        ss += d
        n //= 10

    return ss % 10 == 0


t = int(input())
for _ in range(t):
    n = int(input())
    print("YES" if is_valid(n) else "NO")