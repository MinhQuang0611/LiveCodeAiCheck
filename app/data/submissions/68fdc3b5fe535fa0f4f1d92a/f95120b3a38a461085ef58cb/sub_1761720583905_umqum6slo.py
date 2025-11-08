n = int(input())
a = []
while len(a) < n:
    a.extend(map(int, input().split()))
    gtln = max(a)
    ds = set(a)
    sobm = []
    for i in range(1, gtln +1):
        if i not in ds:
            sobm.append(i)
        if sobm:
            for so in sobm:
                print(sobm)
        else:
            print("Excellent!")