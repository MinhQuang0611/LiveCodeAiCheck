s = input()
opening = 0
for c in s:
    if c == "(":
        opening += 1
    elif c == ")":
        opening -= 1

if opening == 0:
    print("true")
else:
    print("ValueError: Parentheses not balanced")