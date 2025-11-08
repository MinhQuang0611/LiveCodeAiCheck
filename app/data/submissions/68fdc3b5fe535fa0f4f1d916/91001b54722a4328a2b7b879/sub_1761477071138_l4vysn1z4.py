def run_length_encoding(s):
    result = ""
    
    n = len(s)
    i = 0
    while i < n:
        count = 1  
        while i + 1 < n and s[i] == s[i + 1]:
            i += 1
            count += 1
        result += str(count) + s[i]
        i += 1 
    
    return result

t = int(input())

for _ in range(t):
    s = input().strip() 
    print(run_length_encoding(s))  
