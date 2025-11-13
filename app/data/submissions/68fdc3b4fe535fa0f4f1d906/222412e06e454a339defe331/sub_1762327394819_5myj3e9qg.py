t = int(input())
for i in range(t):
    s= input()
    if s[0] == s[-1]:
        print('YES')
    else:
        print('NO')
new_s = s[::-1]
text_new_s = new_s.strip()
text_s = s.strip()