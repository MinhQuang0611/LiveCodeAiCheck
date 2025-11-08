def armstrong(n):
    if n < 0:
        return False
    s = str(n)
    p = len(s)
    sums = 0
    for i in s:
        so = int(i)
        sums += so ** p
    return sums == n
n = int(input())
if armstrong(n):
    print("true")
else:
    print("false")