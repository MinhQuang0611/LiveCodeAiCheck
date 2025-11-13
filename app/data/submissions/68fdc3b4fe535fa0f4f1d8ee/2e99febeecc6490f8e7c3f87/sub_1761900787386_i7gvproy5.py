n = int(input())
arr = []
for i in range(n):
    line = input()
    arr.append(line)
m = ['4','7']
for i in arr:
    check = True
    for j in i:
        if j not in m:
            check = False
            break
    if check == True:
        print("YES")
    else:
        print("NO")
