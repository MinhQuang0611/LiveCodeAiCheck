n = input()
dis = {}
for i in range(0,len(n),2):
	s = n[i:i+2]
	
	dis[s] = 1 + dis.get(s,0)

arr = sorted(dis)
print(arr)

