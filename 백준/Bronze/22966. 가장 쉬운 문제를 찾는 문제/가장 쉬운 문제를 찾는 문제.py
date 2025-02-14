N = int(input())
r = ''
m = 5
for i in range(N):
    a, b = input().split()
    if int(b) < m:
        m = int(b)
        r = a
print(r)