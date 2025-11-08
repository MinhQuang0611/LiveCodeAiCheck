s=input()
s2=s.split()
if len(s2)==len(set(s2)):
    print("true")
else:
    print("false")