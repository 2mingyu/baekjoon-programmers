n = int(input())
s = [0] + list(map(int, input().split()))
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        for x in range(b, n+1, b):
            s[x] = int(not s[x])
    else:
        s[b] = int(not s[b])
        i, j = b-1, b+1
        while i > 0 and j <= n and s[i] == s[j]:
            s[i] = int(not s[i])
            s[j] = int(not s[j])
            i -= 1
            j += 1
for i in range(1, n+1, 20):
    print(*s[i:i+20])