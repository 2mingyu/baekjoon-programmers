T,X=map(int,input().split())
N=int(input())
for _ in range(N):
    K=int(input())
    A=map(int,input().split())
    if X not in A:
        print('NO')
        exit()
print('YES')