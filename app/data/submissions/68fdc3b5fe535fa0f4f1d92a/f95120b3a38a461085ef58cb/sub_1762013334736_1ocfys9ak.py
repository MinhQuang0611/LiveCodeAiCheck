n = int(input())
arr = list(map(int, input().split()))
missing = [i for i in range(1, max(arr)+1) if i not in arr]
print("Excellent!" if not missing else " ".join(map(str,missing)))