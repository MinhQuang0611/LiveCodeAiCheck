w, h, color = input().split()

w = int(w)
h = int(h)

if w <= 0 or h <= 0:
    print("INVALID")
else:
    chu_vi = 2 * (w + h)  
    dien_tich = w * h              
    
    color = color.capitalize() 
    
    print(chu_vi, dien_tich, color)
