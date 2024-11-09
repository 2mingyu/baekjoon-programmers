N = int(input())
K = input()
o = e = 0

for i in K:
    if int(i) % 2:
        o += 1
    else:
        e += 1

if o > e:
    print(1)
elif o < e:
    print(0)
else:
    print(-1)