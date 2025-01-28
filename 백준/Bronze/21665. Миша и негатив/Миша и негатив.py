n, m = map(int, input().split())
r = 0
l = [input() for _ in range(n)]
input()
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == l[i][j]:
            r += 1
print(r)