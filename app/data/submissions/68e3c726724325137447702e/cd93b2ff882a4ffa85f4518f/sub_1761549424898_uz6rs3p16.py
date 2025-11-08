s = input()
ba = 0
for ch in s:
    if ch == '(':
        ba += 1
    elif ch == ')':
        ba -= 1

if ba == 0:
    print("true")
else:
    print("ValueError: Parentheses not balanced")
