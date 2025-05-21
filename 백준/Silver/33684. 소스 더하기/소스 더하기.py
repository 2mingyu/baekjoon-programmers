N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
if A[-1] > K:
    print(0)
elif A[0] <= 0:
    print(-1)
else:
    r = 0
    for i in range(1, N):
        t = (K - A[i]) // A[0]
        A[i] += t * A[0]
        r += t
    t = (K - A[0]) // A[1]
    r += t
    print(r+1)