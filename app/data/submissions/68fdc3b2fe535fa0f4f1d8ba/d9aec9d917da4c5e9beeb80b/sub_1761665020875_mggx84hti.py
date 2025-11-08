n = int(input())
for r in range(n):
    s = input().strip()
    d = [int(a) for a in s]
    con1 = sum(d) % 10 == 0
    if len(d) == 1:
        con2 = True
    else:
        con2 = all(abs(d[i] - d[i+1]) == 2 for i in range(len(d)-1))
    if con1 and con2 :
        print("YES")
    else: 
        print("NO")