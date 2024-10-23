T = int(input())
I = list(map(int, input().split())) + [0] * (5-T)
n = 0
if I[0] > I[2]:
    n += (I[0] - I[2]) * 508
else:
    n += (I[2] - I[0]) * 108
if I[1] > I[3]:
    n += (I[1] - I[3]) * 212
else:
    n += (I[3] - I[1]) * 305
n += I[4] * 707
print(n * 4763)