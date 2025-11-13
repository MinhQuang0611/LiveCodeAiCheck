a = int(input())
for n in range(a):
    s = input()
    dem = 1
    ket_qua = ""

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            dem += 1
        else:
            ket_qua += str(dem) + s[i - 1]
            dem = 1
    ket_qua += str(dem) + s[-1]
    print(ket_qua, end= "")        

            
        