l = sorted(list(map(int, input().split())))
while l[2] >= l[0] + l[1]:
    l[2] -= 1
print(sum(l))