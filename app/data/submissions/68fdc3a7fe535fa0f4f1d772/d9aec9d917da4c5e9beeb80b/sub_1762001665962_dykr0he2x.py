valid = []
def b(s):
    if len(s) > 10:
        return
    if len(s) > 0 and s[0] in ('1', '2'):
        if s.count('2') > len(s) / 2:
            valid.append(int(s))
    for c in '012':
        b(s + c)
b('')
valid.sort()
t = int(input())
for _ in range(t):
    n = int(input())
    print(*valid[:n])