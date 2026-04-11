N = int(input())
data = list(map(int, input().split()))
height = data[0]
r = []
cnt = 0
for i in range(1, N):
    if data[i] < height:
        cnt += 1
    else:
        height = data[i]
        r.append(cnt)
        cnt = 0
r.append(cnt)
print(max(r))