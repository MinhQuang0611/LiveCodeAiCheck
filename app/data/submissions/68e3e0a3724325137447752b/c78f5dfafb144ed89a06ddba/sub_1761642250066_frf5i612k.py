a=input() 
b=input() 
if a.find(".") == -1 and b.find(".") == -1: 
    numa = int(a) 
    numb = int(b) 
    print(numa+numb) 
else: 
    numa=float(a) 
    numb=float(b) 
    print(numa+numb)