N = int(input())
l = dict()
for _ in range(N):
    tmp = int(input())
    if tmp not in l: l[tmp] = 1
    else: l[tmp] += 1
ll = dict(sorted(l.items()))
max_value = 0
for i in ll:
    if ll[i] > max_value:
        result = i
        max_value = ll[i]
print(result)