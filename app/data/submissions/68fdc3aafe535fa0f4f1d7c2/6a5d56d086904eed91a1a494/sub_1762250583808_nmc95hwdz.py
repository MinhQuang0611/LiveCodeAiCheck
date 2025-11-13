n = input()
sl = int(len(n))
ckd = [0] * int((sl /2))
a = 0
for i in range(0,sl,2):
    ckd[a] = int(n[i]) * 10 + int(n[i+1]) 
    a = a + 1
sapxep = set(ckd)

sapxep = list(sapxep)
sapxep.sort()
sl = len(sapxep)




for j in range(0,sl):
    if (j != sl-1):
        print(sapxep[j],end = ' ')
    else:
        print(sapxep[j])
