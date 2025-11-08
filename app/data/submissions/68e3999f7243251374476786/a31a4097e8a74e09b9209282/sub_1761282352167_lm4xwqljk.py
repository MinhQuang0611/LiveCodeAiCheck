n=input()
if(n[0]=='-'):
	n=n.replace("-","")
	print(int(n[::-1])*-1)
else: print(int(n[::-1]))