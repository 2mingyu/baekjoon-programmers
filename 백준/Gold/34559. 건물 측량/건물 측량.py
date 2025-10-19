I=open(0).readline
N,M=map(int,I().split())
m=[list(I())for _ in range(N)]
q=[(0,0)]
while q:
 y,x=q.pop()
 for a,b in((y-1,x),(y+1,x),(y,x-1),(y,x+1)):
  if 0<=a<N and 0<=b<M and m[a][b]=='0':m[a][b]='2';q+=[(a,b)]
s=[[0]*(M+1)for _ in range(N+1)]
for i in range(N):
 for j in range(M):s[i+1][j+1]=s[i][j+1]+s[i+1][j]-s[i][j]+(m[i][j]!='2')
for _ in'0'*int(I()):a,b,c,d=map(int,I().split());t=s[c][d]-s[a-1][d]-s[c][b-1]+s[a-1][b-1];print(('Yes','No %d'%t)[t>0])