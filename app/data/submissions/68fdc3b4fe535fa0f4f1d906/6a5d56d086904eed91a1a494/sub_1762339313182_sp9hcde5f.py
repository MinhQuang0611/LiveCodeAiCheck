n = int(input())
ds = n*[0]
for i in range(0,n):
    ds[i] = input()
for j in range(0,n):
    sl = len(ds[j])
    tam = ds[j]
    if (tam[0] == tam[sl-1]):
        print("YES")
    else:
        print("NO")
    