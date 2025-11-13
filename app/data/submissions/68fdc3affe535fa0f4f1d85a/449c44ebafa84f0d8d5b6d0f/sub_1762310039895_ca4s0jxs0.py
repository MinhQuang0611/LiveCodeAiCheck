if __name__ == '__main__':
    t = int(input())
    n = int(input())
    for _ in range(t):
        danh_sach = []
        for _ in range(n):
            a,b = map(int, input().split())
            danh_sach.append([a,b])
        danh_sach.sort(key = lambda x: x[0])
        danh_sach2 = []
        for x in danh_sach:
            danh_sach2.append(x[1])
        cnt = 1
        for i in range(1, len(danh_sach2)):
            if danh_sach2[i] < danh_sach2[i - 1]:
                cnt += 1
            else:
                break
        print(cnt)