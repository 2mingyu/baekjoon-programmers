"""
정수 삼각형
현재 칸으로 올 경로는 전의 두 칸 중 max로 결정
"""
n = int(input())
t = []
m = []
for _ in range(n):
    l = list(map(int, input().split()))
    t.append([0] + l)
    m.append([0] + l + [0])
for i in range(1, n):
    for j in range(1, i+2):
        m[i][j] = t[i][j] + max(m[i-1][j-1], m[i-1][j])
print(max(m[n-1]))