M = int(input())
N = int(input())
l = []
for i in range(M, N+1):
    if i**0.5 == int(i**0.5):
        l.append(i)
if len(l):
    print(sum(l))
    print(l[0])
else:
    print(-1)