def demktsl(n):
    if not n:
        return ""
    arr = []
    cnt=1 
    kt = n[0]
    for i in n[1:]:
        if i == kt:
            cnt +=1
        else:
            arr.append(str(cnt) + kt)
            kt = i
            cnt = 1
    arr.append(str(cnt)+kt)
    return "".join(arr)
t = int(input())
for _ in range(t):
    n= input().rstrip("\n")
    print(demktsl(n))