def is_repeat(n: int):
    s = set()
    while n > 0:
        d = n % 10
        if d in s:
            return True
        s.add(d)
        n //= 10
    return False

n = int(input())
print("true" if is_repeat(n) else "false")