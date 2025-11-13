n = int(input())

for i in range (0, n):
	flag = False
	s = input()
	if s[0] == s[-1]: flag = True
	if flag: print("YES")
	else: print("NO")