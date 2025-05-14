a = 0
b = 0
N = int(input())
l = list(map(int, input().split()))
for e in l:
    if e: a += 1
    else: a -= 1
    b += a
print(b)