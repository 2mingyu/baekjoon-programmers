C, n = map(int, input().split())

x = 0
r = 'possible'
w = 0

for i in range(n):
    a, b, c = map(int, input().split())
    x -= a
    if x < 0:
        r = 'impossible'
    x += b
    if x > C:
        r = 'impossible'
    if c > 0 and x < C:
        r = 'impossible'
    if i == n - 1:
        w = c

if x != 0 or w != 0:
    r = 'impossible'

print(r)