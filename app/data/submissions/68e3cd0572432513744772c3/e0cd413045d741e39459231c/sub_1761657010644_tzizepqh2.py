a=int(input())
s=str(a)
lap='false'
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        lap='true'
        break
print(lap)