binary_str = input()
a  = 3 - len(binary_str)%3 
new_n = '0'*a + binary_str 
oct_final = ''
for i in range(0,len(new_n),3): 
    oct_count = new_n[i:i+3]
    oct_digit = str(int(oct_count,2))  sang số bát phân
    oct_final += oct_digit 
print(oct_final)