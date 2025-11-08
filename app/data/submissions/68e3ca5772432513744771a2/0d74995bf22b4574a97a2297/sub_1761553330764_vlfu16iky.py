def ktr(n, so):
    s = str(n)
    if s != s[::-1]:
        return False
    res = set(str(d) for d in so)
    if not set(s).issubset(res):
        return False
    return True
n = input()
d = list(input())
if(ktr(n,d)):
    print("True")
else:
    print("False")