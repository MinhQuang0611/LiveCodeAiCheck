import math
import string
n=input()
IN=n.split(" ")
def chuyendoi(ex):
	c=0
	for i in ex:
		c*=10
		c+=int(i)+int('0')
	return c
a=chuyendoi(IN[0])
b=chuyendoi(IN[1])
print(a-b)