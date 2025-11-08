n=int(input())
mn=9999999
mx=-9999999
tong=0
lst=input().split()
for i in lst:
	tong+=int(i)
	mx=max(int(i),mx)
	mn=min(int(i),mn)
print((tong-mx-mn)/(n-2))