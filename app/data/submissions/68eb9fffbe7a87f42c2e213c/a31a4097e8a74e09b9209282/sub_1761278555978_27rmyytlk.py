import math
import string
n=input()
IN=n.split(" ")
def chuyendoi(ex):
	check=0
	if(ex[0]=='-'): 
		check=1
		ex=ex.replace("-","")
	c=0
	for i in ex:
		c*=10
		c+=int(i)+int('0')
	if (check==1):
		return -c
	else:
		return c
a=chuyendoi(IN[0])
b=chuyendoi(IN[1])
print(a+b)