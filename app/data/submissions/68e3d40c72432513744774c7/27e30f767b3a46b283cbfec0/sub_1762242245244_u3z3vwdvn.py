num_1 = int(input())
ar_1 = list(map(int, input().split()))
num_2 = int(input())
ar_2 = list(map(int, input().split()))
lst = []
for i in ar_2:
    if i in ar_1:
        lst.append(i)
lst.sort()
print(*lst)