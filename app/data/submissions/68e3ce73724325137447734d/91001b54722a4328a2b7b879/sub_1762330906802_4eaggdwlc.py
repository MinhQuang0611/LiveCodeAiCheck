columnNumber = int(input())
result = ""
while columnNumber > 0:
    columnNumber -= 1 
    result = chr(columnNumber % 26 + ord('A')) + result
    columnNumber //= 26
print(result)
