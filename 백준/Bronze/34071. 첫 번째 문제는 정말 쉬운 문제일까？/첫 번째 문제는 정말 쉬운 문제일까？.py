N = int(input())
X = [int(input()) for _ in range(N)]
if X[0] == min(X):
    print('ez')
elif X[0] == max(X):
    print('hard')
else:
    print('?')