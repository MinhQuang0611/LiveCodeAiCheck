line = input().split()
w = int(line[0])
h = int(line[1])
color = line[2]
if w <= 0 or h <= 0:
    print("INVALID")
else:
    perimeter = 2 * (w + h)
    area = w * h
    normalized_color = color.capitalize()
    print(perimeter, area, normalized_color)
