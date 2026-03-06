N = int(input())
H = list(map(int, input().split()))
r = 1
for i in range(1, N):
    if H[i-1] <= H[i]:
        r += 1
print(r)