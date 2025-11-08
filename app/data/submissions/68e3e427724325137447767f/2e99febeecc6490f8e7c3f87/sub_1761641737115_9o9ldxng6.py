s = input()
a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count = 0
for i in s:
    if i in a:
        count+=1
print(count)