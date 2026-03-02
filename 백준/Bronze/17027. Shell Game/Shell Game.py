N = int(input())
s = [1, 2, 3]
r = [0, 0, 0]
for _ in range(N):
    a, b, g = map(int, input().split())
    for i in range(len(s)):
        if s[i] == a: s[i] = b
        elif s[i] == b: s[i] = a
        if s[i] == g: r[i] += 1
print(max(r))