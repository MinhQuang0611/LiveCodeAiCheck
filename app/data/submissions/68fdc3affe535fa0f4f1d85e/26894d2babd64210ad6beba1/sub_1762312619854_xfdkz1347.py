def check(n):
    if n[0] != '6':
        return False
    for i in n:
        if i != '6' and i != '8':
            return False
    for i in range(len(n) - 2):
        if n[i] == n[i + 1] == n[i + 2] == '8':
            return False

    return True
n = input().strip()
if check(n):
    print("YES")
else:
    print("NO")
def check(n):
    if n[0] != '6':
        return False
    for i in n:
        if i != '6' and i != '8':
            return False
    for i in range(len(n) - 2):
        if n[i] == n[i + 1] == n[i + 2] == '8':
            return False

    return True
n = input().strip()
if check(n):
    print("YES")
else:
    print("NO")
