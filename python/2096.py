"""
내려가기
"""
N = int(input())
l = list(map(int, input().split()))
dp_min, dp_max = [0,0,0], [0,0,0]
for i in range(3): dp_min[i] = dp_max[i] = l[i]
for _ in range(N-1):
    l = list(map(int, input().split()))
    dp_min = [min(dp_min[0:2])+l[0], min(dp_min[0:3])+l[1], min(dp_min[1:3])+l[2]]
    dp_max = [max(dp_max[0:2])+l[0], max(dp_max[0:3])+l[1], max(dp_max[1:3])+l[2]]
print(max(dp_max), min(dp_min))