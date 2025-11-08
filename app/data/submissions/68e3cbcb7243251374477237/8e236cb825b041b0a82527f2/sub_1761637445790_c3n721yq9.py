def modulo(s):
    if len(s) == 0:
        return 0
    
    return sum(ord(c) for c in s) % 1000000007

print(modulo(input()))