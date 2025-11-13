A=list(input().split())
for char in range(len(A)):
    new=""
    for i in A[char]:
        if not(i.isalnum() or i==":" or i==","):
            continue
        new+=i
    A[char]=new
s=""
for i in A:
    if i!="":
        s+=i+" "
print(s.title())