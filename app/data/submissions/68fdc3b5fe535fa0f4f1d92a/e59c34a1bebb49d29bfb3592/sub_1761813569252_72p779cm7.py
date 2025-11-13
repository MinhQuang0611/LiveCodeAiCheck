n = int(input())
arr = list(map(int,input().split()))
t = [i for i in range(1,max(arr)+1) if i not in arr]
print("Excellent!" if not t else " ".join(map(str,t)))
