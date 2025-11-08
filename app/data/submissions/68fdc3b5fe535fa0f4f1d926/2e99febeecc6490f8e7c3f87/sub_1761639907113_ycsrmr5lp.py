def gt(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*gt(n-1)

def sinh_hoan_vi(s,prefix = ""):
    if len(s) == 0:
        print(prefix, end=" ")
    else:
        for i in range(len(s)):
            a = s[:i] + s[i+1:]
            sinh_hoan_vi(a,prefix + s[i])
def tao_chuoi(n):
    s = ""
    for i in range(1,n+1):
        a = str(i)
        s += a
    return s
if __name__ == '__main__':
    t = int(input(""))
    n = int(input(""))
    print(gt(n))
    tao_chuoi(n)
    sinh_hoan_vi(tao_chuoi(n),prefix = "")
    print()
