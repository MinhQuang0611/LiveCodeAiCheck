t = int(input()) 
strings = [input().strip() for _ in range(t)]
results = []
for s in strings:
    result = ""
    for i in range(0, len(s), 2):  
        char = s[i]
        count = int(s[i+1])
        result += char * count
    results.append(result)
for res in results:
    print(res)
