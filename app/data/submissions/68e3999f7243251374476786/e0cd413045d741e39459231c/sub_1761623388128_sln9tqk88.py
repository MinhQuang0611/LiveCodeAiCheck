a=int(input('nhập số cần kiểm tra:'))
s=str(a)
lap=False
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        lap=True
        break
print(lap)