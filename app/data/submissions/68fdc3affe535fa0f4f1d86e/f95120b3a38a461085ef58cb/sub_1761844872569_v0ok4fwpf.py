t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    max_strength = max(lst)
index = lst.index(max_strength)
lst.insert(index, k)
lst_am = []
lst_duong = []
for i in lst:
    if i < 0:
        lst_am.append(i)
    else:
        lst_duong.append(i)
print(*lst_am, *lst_duong)