"""
소수의 연속합
"""
N = int(input())

if N == 1:
    print(0)
    exit()

l = [1]*(N+1)
l[0] = l[1] = 0
for i in range(2, N+1):
    if l[i]:
        ii = i + i
        while ii < N+1:
            l[ii] = 0
            ii += i

p = []
for i in range(N+1):
    if l[i]: p.append(i)

s = e = 0
r = 0
t = p[0]
while True:
    if t < N:
        if e == len(p)-1: break
        e += 1
        t += p[e]
    elif t > N:
        t -= p[s]
        s += 1
    else:
        r += 1
        if e == len(p)-1: break
        e += 1
        t += p[e]

print(r)