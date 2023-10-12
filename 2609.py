"""
최대공약수와 최소공배수
"""
a,b=map(int,input().split())
m=min(a,b)
i=m
while 1:
    if a%i+b%i==0:
        print(i)
        break
    i-=1
i=m
while 1:
    if i%a+i%b==0:
        print(i)
        break
    i+=m