"""
거스름돈
"""
N=1000-int(input())
r=0
for n in 500,100,50,10,5,1:
 r+=N//n
 N=N%n
print(r)