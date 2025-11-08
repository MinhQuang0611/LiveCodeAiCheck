n = input()
n = n.lower()
m=list(n)
count=0
for i in range(len(m)):    
    if "a" in m or "e" in m or "i" in m or "o" in m or "u" in m:
        count+=1
print(count)
