a, b, c, d = map(int, input().split())
dem = 0
while not (a == b and b == c and c == d):
 a1 , b1 , c1 , d1 = a , b , c ,d
 a = abs (a1-b1)
 b = abs (b1-c1)
 c = abs (c1-d1)
 d = abs (d1-a1)
 dem+=1
print (dem)