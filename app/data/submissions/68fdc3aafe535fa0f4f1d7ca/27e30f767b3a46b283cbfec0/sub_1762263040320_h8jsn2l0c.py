n = input()
lst = [x for x in n]
count = len(n) // 3
i = 1
while count != 0:
    lst.insert(-4*i+1,',')
    count -= 1
    i+=1
if lst[0] == ',':
    lst.pop(0)
ans = ''.join(x for x in lst)
print(ans)