def xu_ly(_str):
    width, height, colour = map(str, _str.split())
    w = int(width)
    h = int(height)
    if w <= 0 or h <= 0:
        return "INVALID"
    else: 
        return f"{(w+h)*2} {w*h} {colour.strip().title()}"

string = input()
print(xu_ly(string))