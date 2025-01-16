N = int(input())
l = [False]*(N+1)
r = 0
s = 0
for i in list(map(int, input().split())):
    if l[i]:
        l[i] = False
        s -= 1
    else:
        l[i] = True
        s += 1
        r = max(s, r)
print(r)