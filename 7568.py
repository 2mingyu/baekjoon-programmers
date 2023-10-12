"""
덩치
"""
N=int(input())
p=[]
for _ in range(N):p.append(list(map(int,input().split())))
a=[0]*N
for i in range(N):
    for j in range(N):
        if p[i][0]<p[j][0] and p[i][1]<p[j][1]:a[i]+=1
for i in a:print(i+1,end=" ")