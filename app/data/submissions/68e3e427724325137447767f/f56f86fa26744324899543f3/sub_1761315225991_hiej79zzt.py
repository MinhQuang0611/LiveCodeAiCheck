a=["a","e","i","o","u"]
s=input()
count=0
for i in s:
    if i.lower() in a:count+=1
print(count)