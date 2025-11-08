n=input()
if n[0] == '-':
    result = '-' + n[:0:-1]
else:
    result = n[::-1]
print(result)