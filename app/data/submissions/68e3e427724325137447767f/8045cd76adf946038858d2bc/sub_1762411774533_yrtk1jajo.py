n=input().lower()
count=0
for char in n:
    if char in 'aeiou':
        count +=1
print(count)
