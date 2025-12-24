n = int(input())
f = t = 0

while True:
    if n%5 == 0:
        f = n // 5
        break
    n -= 2
    t += 1
    if n < 0:
        print(-1)
        exit()

print(f+t)