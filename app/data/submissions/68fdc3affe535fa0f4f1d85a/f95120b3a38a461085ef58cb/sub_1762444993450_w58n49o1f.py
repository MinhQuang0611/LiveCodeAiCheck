t = int(input())
for _ in range(t):
    nui = int(input())     
    ds_nui = []   
    for i in range(nui):
        dl = input().split()
        cao = float(dl[0]) 
        kho = float(dl[1]) 
        ds_nui.append((cao, kho))
    if nui == 0:
        print(0)
        continue  
    dp = [1] * nui
    dai_max = 0
    for i in range(nui):
        cao_i, kho_i = ds_nui[i]       
        for j in range(i):
            cao_j, kho_j = ds_nui[j]            
            if cao_j < cao_i and kho_j > kho_i:
                dp[i] = max(dp[i], dp[j] + 1)       
        dai_max = max(dai_max, dp[i])
    print(dai_max)