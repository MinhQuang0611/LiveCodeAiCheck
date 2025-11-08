t = int(input())
for i in range(t):
    s = input().strip()
    result = ""
    count = 1
    
    for j in range(1, len(s)):
        if s[j] == s[j-1]:
            count += 1
        else:
            result += str(count) + s[j-1]
            count = 1
    result += str(count) + s[-1]  
    print(result)
