n = int(input())
signs = set()  
for i in range(n):
    s = input().strip()
    if s != "-1": 
        signs.add(s)
print(len(signs))