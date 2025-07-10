l = list(map(int, input().split()))
r = 0
for e in l[1:]:
    if l[0]-e <= 1000:
        r += 1
print(r)