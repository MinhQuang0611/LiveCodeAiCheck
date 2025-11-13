s = input()
opening = 0
for c in s:
    if opening < 0:
        break

    if c == "(":
        opening += 1
    elif c == ")":
        opening -= 1

if opening == 0:
    print("true")
else:
    # raise ValueError("Parentheses not balanced")
    print("ValueError: Parentheses not balanced")