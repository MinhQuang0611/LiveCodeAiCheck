#n = int(input())
dayso = list(map(int,input().split()))
if not dayso:
    print("0.0")
else:
    tong = sum(dayso)
    print(tong/len(dayso))
