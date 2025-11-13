s = input().strip() 

s_nguoc = s[::-1]

a = [s_nguoc[i:i+3] for i in range(0, len(s_nguoc), 3)]

result_nguoc = ','.join(a)

result = result_nguoc[::-1]

print(result)