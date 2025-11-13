n = int(input())
lst = []
for i in range(n):
    s = input()
    if s not in lst:
        lst.append(s)
print(len(lst))



