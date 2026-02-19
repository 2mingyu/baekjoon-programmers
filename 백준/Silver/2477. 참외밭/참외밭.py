K = int(input())
d = []
l = []
for _ in range(6):
    a, b = map(int, input().split())
    d.append(a)
    l.append(b)

mx_w = 0
mx_h = 0
iw = -1
ih = -1

for i in range(6):
    if d[i] <= 2:
        if l[i] > mx_w:
            mx_w = l[i]
            iw = i
    else:
        if l[i] > mx_h:
            mx_h = l[i]
            ih = i

sw = abs(l[(ih-1) % 6] - l[(ih+1) % 6])
sh = abs(l[(iw-1) % 6] - l[(iw+1) % 6])

r = mx_w * mx_h - sw * sh
print(r * K)