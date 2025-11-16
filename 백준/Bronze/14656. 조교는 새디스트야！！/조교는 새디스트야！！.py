N = int(input())
l = list(map(int, input().split()))
c = 0
for i in range(N):
    if l[i] != i+1: c += 1
print(c)