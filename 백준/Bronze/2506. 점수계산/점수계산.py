N = int(input())
l = list(map(int, input().split()))
for i in range(1, N):
    if l[i]:
        if l[i-1] == 0: l[i] = 1
        else: l[i] = l[i-1]+1
print(sum(l))