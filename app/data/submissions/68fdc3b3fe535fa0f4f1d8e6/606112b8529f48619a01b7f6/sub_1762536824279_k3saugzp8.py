w, h, color = map(str, input().split())
w=int(w)
h=int(h)
if w > 0 and h > 0:
    print(f'{(w+h)*2} {w*h} {color.title()}')
else: 
    print('INVALID')