n = int(input())
cnt = []  
for i in range(n + 1):   
    binary_str = bin(i)   
    ones = binary_str.count('1') 
    cnt.append(ones)      
print(cnt)
