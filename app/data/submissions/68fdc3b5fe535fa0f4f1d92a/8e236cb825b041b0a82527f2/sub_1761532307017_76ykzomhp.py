n = int(input())
nums = []

while len(nums) < n:
    sz = len(nums)
    inp = list(map(int, input().split()))[: n - sz]
    nums += inp

s1 = set(nums)
miss = False

for i in range(1, max(nums)):
    if i not in s1:
        print(i)
        miss = True

if not miss:
    print("Excellent!")
