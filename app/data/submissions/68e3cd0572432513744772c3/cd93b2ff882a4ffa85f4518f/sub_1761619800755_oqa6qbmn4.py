n = input()
has_repeat = False 
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:     
        has_repeat = True
        break          

if has_repeat:
    print("true")
else:
    print("false")