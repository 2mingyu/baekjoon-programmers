N = int(input())
l = [[]] + [list(map(int, input().split())) for _ in range(N)]
M = int(input())
if M > 0:
    s = set([0] + list(map(int, input().split())))
else:
    s = {0}
r = 0
for i in range(N):
    if i+1 not in s and l[i+1][0] not in s and l[i+1][1] not in s:
        r += 1
print(r)