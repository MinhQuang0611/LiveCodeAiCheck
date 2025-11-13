n=input().strip()
a='!.&'
b=''
for i in n:
    if i not in a:
        b+=i
b=b.lower()
b = ' '.join(b.split())
print(b.title())