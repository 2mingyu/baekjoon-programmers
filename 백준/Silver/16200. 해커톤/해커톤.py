N = int(input())
X = list(map(int, input().split()))
X.sort()
r = 0
t = X[0]
for i in range(N):
    if t:
        t -= 1
    else:
        r += 1
        t = X[i]-1
print(r+1)