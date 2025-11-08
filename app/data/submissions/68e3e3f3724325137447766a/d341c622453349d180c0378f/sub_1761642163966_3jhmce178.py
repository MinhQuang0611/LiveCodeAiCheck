n=int(input())
sodaonguoc=0
while n>0:
    chusocuoi=n%10
    sodaonguoc=sodaonguoc*10+chusocuoi
    n=n//10
print(sodaonguoc)