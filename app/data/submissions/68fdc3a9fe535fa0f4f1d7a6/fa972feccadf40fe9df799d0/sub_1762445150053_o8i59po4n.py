t = int(input())
for _ in range(t):
    s = input()
    import re
    a = re.findall(r'\d+', s)
    b = [int(x) for x in a]
    c = min(b)
    print(c)