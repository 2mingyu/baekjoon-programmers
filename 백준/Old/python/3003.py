"""
킹, 퀸, 룩, 비숍, 나이트, 폰
"""
i=list(map(int,input().split()))
print(1-i[0],1-i[1],2-i[2],2-i[3],2-i[4],8-i[5])

a=[1,1,2,2,2,8]
b=input().split()
for i in range(6): print(a[i]-int(b[i]),end=" ")