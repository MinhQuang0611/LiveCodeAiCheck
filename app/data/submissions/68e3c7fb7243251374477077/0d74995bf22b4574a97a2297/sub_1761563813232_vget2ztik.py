n = input()
m = sum(int(digit) for digit in n)
if(m % 3 == 0):
    d = list(n)
    d.sort(reverse= True)
    res = "".join(d)
    print(res)
else:
    print(-1)
