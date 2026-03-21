n = int(input())
v = [0] * (n + 1)
x = 1
v[1] = 1

while 1:
    y = (x * 2) % n
    if y == 0:
        y = n
    if y == 1 or v[y]:
        print(x)
        break
    v[y] = 1
    x = y