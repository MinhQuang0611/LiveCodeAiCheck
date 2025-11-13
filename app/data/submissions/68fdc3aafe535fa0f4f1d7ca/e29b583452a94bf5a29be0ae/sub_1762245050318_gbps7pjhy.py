s = input()
s = s[::-1]      
result = []
for i in range(len(s)):
    if i > 0 and (len(s) - i) % 3 == 0:
        result.append(',')
    result.append(s[i])
print(''.join(result))