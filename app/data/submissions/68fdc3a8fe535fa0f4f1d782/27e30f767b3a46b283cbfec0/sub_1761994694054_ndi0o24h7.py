array = input()
copy = array[:]
num = int(input())
dic = {}
lst = []
check = False

while len(copy) > 0:
    lst.append(copy[:2])
    copy = copy[2:]
for i in range(len(lst)):
    if lst[i] not in dic:
        dic[lst[i]] = 1
    else:
        dic[lst[i]]  += 1
for key,value in dic.items():
    print(key,value)
    if value >= num:
        check = True
if not check:
    print('NOT FOUND')

