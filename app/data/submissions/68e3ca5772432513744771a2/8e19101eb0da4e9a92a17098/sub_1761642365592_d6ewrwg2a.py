def check(n, digits):
    s = str(n)
    return s == s[::-1] and all(int(ch) in digits for ch in s)
n = int(input())
digits = input()
digits = digits.strip("[]")
p = [x.strip() for x in digits.split(",") if x.strip() != ""]
digits = list(map(int, p))
print(check(n, digits))