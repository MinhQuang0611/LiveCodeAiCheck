arr = list(map(int,input().split()))
if len(arr) <= 0:
    print("0.0")
else:
    print(sum(arr)/len(arr))