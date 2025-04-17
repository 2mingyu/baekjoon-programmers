P = int(input())
N = int(input())
R = int(input())
i = 0
s = N
b = N
while s <= P:
    i += 1
    s += b*R
    b *= R
print(i)