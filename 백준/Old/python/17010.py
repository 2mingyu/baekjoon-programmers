"""
Time to Decompress
"""
L = int(input())
for _ in range(L):
    S = input().split()
    N = int(S[0])
    x = S[1]
    print(N*x)