n=int(input())
n=str(n)
k="false"
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        k="true"
        break
print(k)