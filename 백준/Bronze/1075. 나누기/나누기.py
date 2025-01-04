N = int(input())
F = int(input())

a = N // 100 * 100
for i in range(100):
    if a % F == 0:
        break
    a += 1
print(str(a)[-2:])