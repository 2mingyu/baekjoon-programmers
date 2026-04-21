N = int(input())
r = 0
for _ in range(N):
    s = input()
    if s[0] == 'C':
        r += 1
print(r)