t = int(input())
count = 0
for x in range(t):
    s = input().strip()
    for i in s:
        if i == "4" or i == "7":
            count += 1
    if count == len(s):
        print("YES")
    else:
        print("NO")
    count = 0