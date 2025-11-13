t = int(input().strip())
for _ in range(t):
    s = input().strip()
    p = 1
    sum_even = 0
    kiemtra = False
    for i in range(len(s)):
        chuso = int(s[i])
        vitri = i + 1
        if vitri % 2 == 1:
            if chuso != 0:
                p *= chuso
                kiemtra = True
        else:
            sum_even += chuso
    if not kiemtra:
        p = 0
    print(p, sum_even)
