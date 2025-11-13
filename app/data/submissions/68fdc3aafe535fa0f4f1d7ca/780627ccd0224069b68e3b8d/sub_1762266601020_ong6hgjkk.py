def dequy(s):
    if len(s) <= 3:
        return s
    return dequy(s[:-3]) + ',' + s[-3:]
s = input()
print(dequy(s))