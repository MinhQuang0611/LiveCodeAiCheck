import sys 
input = sys.stdin.read
data = input().split()
t= int(data[0])
for i in range(1, t+1):
    n = int(data[i])
    print("YES"if n % 3 ==0 else"NO")