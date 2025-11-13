t = int(input())
for _ in range(t):
    s = input()
    nums = re.findall(r'\d+', s)
    print(min(map(int, nums)) if nums else "Không có số nào trong chuỗi")