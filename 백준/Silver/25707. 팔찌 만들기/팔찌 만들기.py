N = int(input())
M = sorted(map(int, input().split()))
s = M[-1] - M[0]
for i in range(1, N):
    s += M[i] - M[i-1]
print(s)