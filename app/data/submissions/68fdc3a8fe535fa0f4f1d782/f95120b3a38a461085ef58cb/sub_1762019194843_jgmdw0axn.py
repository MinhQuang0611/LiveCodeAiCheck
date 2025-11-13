import collections
import sys

def solve():
    try:
        a = sys.stdin.readline().strip()
        if not a:
            return
        
        n_str = sys.stdin.readline().strip()
        if not n_str:
            print("NOT_FOUND")
            return
            
        n = int(n_str)
        
    except Exception:
        return

    dic = collections.Counter()
    len_a = len(a)
    
    if len_a < 2:
        print("NOT_FOUND")
        return

    for i in range(0, len_a - 1, 2):
        cap = a[i:i+2]
        dic[cap] += 1
        
    ket_qua_loc = []
    for cap, tan_suat in dic.items():
        if tan_suat >= n:
            ket_qua_loc.append((cap, tan_suat))
            
    ket_qua_loc.sort(key=lambda x: x[0])

    if not ket_qua_loc:
        print("NOT_FOUND")
    else:
        for cap, tan_suat in ket_qua_loc:
            print(f"{cap} {tan_suat}")

if __name__ == "__main__":
    solve()