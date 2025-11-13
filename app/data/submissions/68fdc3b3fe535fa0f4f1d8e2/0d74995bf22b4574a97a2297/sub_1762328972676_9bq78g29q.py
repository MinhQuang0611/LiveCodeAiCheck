def solve():
        d, m = map(int, input().split())
        chom_sao = ""
        if m == 1:
            if d <= 19:
                chom_sao = "Ma Ket"
            else:
                chom_sao = "Bao Binh"
        elif m == 2:
            if d <= 18:
                chom_sao = "Bao Binh"
            else:
                chom_sao = "Song Ngu"
        elif m == 3:
            if d <= 20:
                chom_sao = "Song Ngu"
            else:
                chom_sao = "Bach Duong"
        elif m == 4:
            if d <= 19:
                chom_sao = "Bach Duong"
            else:
                chom_sao = "Kim Nguu"     
        elif m == 5:
            if d <= 20:
                chom_sao = "Kim Nguu"
            else:
                chom_sao = "Song Tu"                
        elif m == 6:
            if d <= 21:
                chom_sao = "Song Tu"
            else:
                chom_sao = "Cu Giai"               
        elif m == 7:
            if d <= 22:
                chom_sao = "Cu Giai"
            else:
                chom_sao = "Su Tu"                
        elif m == 8:
            if d <= 22:
                chom_sao = "Su Tu"
            else:
                chom_sao = "Xu Nu"                
        elif m == 9:
            if d <= 22:
                chom_sao = "Xu Nu"
            else:
                chom_sao = "Thien Binh"                
        elif m == 10:
            if d <= 23:
                chom_sao = "Thien Binh"
            else:
                chom_sao = "Bo "                
        elif m == 11:
            if d <= 21:
                chom_sao = "Bo Cap"
            else:
                chom_sao = "Thien Yet"               
        elif m == 12:
            if d <= 21:
                chom_sao = "Thien Yet"
            else:
                chom_sao = "Ma Ket"
        print(chom_sao)
t = int(input())
for _ in range(t):
    solve()