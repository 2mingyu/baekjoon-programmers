"""
분수 찾기

a,b=1,1
for i in range(1,int(input())):
    if (a+b)%2:
        if b==1: a+=1
        else:
            a+=1
            b-=1
    else:
        if a==1: b+=1
        else:
            a-=1
            b+=1
print(str(a)+'/'+str(b))

시간초과

https://codesyun.tistory.com/58
"""
X=int(input())
i=1
while i<X:
    X-=i
    i+=1
a=str(i+1-X)
b=str(X)
if i%2:print(a+'/'+b)
else:print(b+'/'+a)