n = int(input())
temp, oxy, ocean = -30, 0, 0
for _ in range(n):
    p, v = input().split()
    v = int(v)
    if p == 'temperature': temp += v
    elif p == 'oxygen': oxy += v
    else: ocean += v
print('liveable' if temp >= 8 and oxy >= 14 and ocean >= 9 else 'not liveable')