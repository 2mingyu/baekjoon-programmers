Q1 = Q2 = Q3 = Q4 = AXIS = 0
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if y > 0:
        if x > 0: Q1 += 1
        elif x < 0: Q2 += 1
        else: AXIS += 1
    elif y < 0:
        if x < 0: Q3 += 1
        elif x > 0: Q4 += 1
        else: AXIS += 1
    else: AXIS += 1
print('Q1:', Q1)
print('Q2:', Q2)
print('Q3:', Q3)
print('Q4:', Q4)
print('AXIS:', AXIS)
