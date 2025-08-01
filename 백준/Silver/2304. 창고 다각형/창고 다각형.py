N = int(input())
M = [0]*1001
minL, maxL, midL = 1000, 0, -1
maxH = 0
for _ in range(N):
    L, H = map(int, input().split())
    M[L] = H
    minL = min(L, minL)
    maxL = max(L, maxL)
    if H > maxH:
        maxH = H
        midL = L
r = maxH
tmpH = 0
for L in range(minL, midL):
    tmpH = max(M[L], tmpH)
    r += tmpH
tmpH = 0
for L in range(maxL, midL, -1):
    tmpH = max(M[L], tmpH)
    r += tmpH
print(r)