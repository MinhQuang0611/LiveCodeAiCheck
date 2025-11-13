t = int(input())
for _ in range(t):
    lst_height = []
    lst_rate = []
    way = 1
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        lst_height.append(a)
        lst_rate.append(b)
    for i in range(n-1):
        if lst_height[i]<=lst_height[i+1] and lst_rate[i]>=lst_rate[i+1]:
            way += 1
        else:
            break
print(way)
