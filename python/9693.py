"""
시파르

10 = 2 * 5
"""
l2 = [0]
l5 = [0]
for i in range(1, 10**6 + 1):
    n = i
    n2 = 0
    while not n % 2:
        n //= 2
        n2 += 1
    l2.append(n2 + l2[-1])
    n = i
    n5 = 0
    while not n % 5:
        n //= 5
        n5 += 1
    l5.append(n5 + l5[-1])
i = 1
while True:
    N = int(input())
    if not N: break
    print('Case #' + str(i) + ':', min(l2[N], l5[N]))
    i += 1