'''
Yêu cầu
Với mỗi chuỗi ký tự được cung cấp, hãy kiểm tra:

Nếu ký tự đầu tiên và ký tự cuối cùng của chuỗi giống nhau, in ra "YES".
Ngược lại, in ra "NO".
'''
t = int(input())
for i in range (t):
    n = input()
    if n[0] == n[-1]:
        print ('YES')
    else:
        print ('NO')