n = int(input())
numbers  = []
for _ in range(n):
    t = input().strip()
    num = ""
    for x in t:
        if x.isdigit(): 
            num += x
        else:
            if num != "":
                numbers.append(int(num))
                num = ""
    if num != "":
        numbers.append(int(num))
numbers.sort()
for i in numbers:
    print(i)  

