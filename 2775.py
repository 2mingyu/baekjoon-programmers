"""
부녀회장이 될테야
"""
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    h=[[i for i in range(n+1)] for _ in range(k+1)]
    for a in range(1,k+1):
        for b in range(1,n+1):
            h[a][b] = sum(h[a-1][i] for i in range(b+1))
    print(h[k][n])
