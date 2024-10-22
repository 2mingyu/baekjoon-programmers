"""
1장 : P1
2장 : 1장+P1 or P2
3장 : 1장+P2 or 2장+P1 or P3
4장 : 1장+P3 or 2장+P2 or 3장+P1 or P4
"""
N = int(input())
P = [0] + list(map(int, input().split()))
m = [0] * (N+1)
for i in range(1, N+1):
    for j in range(1, i+1):
        m[i] = max(m[i], m[i-j] + P[j])
print(m[-1])