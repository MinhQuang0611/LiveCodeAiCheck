n = int(input())
lst = list(map(int, input().split()))

lst = sorted(lst)


lst.remove(lst[0])
lst.remove(lst[-1])

tong = 0
for i in lst:
    tong += i

print(tong/len(lst))