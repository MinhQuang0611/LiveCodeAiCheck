t=int(input())
s=input().strip()
count=1
res=""
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else: 
        res+=str(count) + s[i-1]
        count=1 #reset lại để bắt đầu chuỗi mới
res+=str(count) + s[-1] #xử lí phần tử cuối cùng vì không còn phẩn tử sau để so sánh
print(res)





