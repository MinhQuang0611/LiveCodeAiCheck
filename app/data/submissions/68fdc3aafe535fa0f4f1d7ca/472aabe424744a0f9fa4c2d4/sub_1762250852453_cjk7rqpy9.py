s=input()
result=""
for i in range(len(s)):
    if i >0 and (len(s)-i)%3==0:
        result +=","
    result += s[i]
print(result)