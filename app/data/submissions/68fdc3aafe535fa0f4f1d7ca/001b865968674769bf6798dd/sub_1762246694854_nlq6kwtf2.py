s = input().strip()
s_reversed = s[::-1]
chunks = [s_reversed[i:i+3] for i in range(0, len(s_reversed), 3)]
result = ','.join(chunks)[::-1]
print(result)