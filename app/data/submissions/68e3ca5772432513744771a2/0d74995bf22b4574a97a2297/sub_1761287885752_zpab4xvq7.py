def ktr(n, digits):
    n_str = str(n)
    if n_str != n_str[::-1]:
        return False
    allowed_digits_str = set(str(d) for d in digits)
    if not set(n_str).issubset(allowed_digits_str):
        return False
    return True
n = input()
d = list(input())
if(ktr(n,d)):
    print("True")
else:
    print("False")