s = input()
opening = 0
for c in s:
    if c == "(":
        opening += 1
    elif c == ")":
        opening -= 1

if len(s) > 0 and opening == 0:
    print("true")
else:
    # raise ValueError("Parentheses not balanced")
    print("ValueError: Parentheses not balanced")