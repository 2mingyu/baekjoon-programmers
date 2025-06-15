N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
K = list(map(float, input().split()))
K = [10*k for k in K]
r = 0
for i in range(N):
    t1 = A[i]*K[i]//10 - B[i]
    t2 = A[i] - B[i]*K[i]//10
    r += max(t1, t2)
print(int(r))