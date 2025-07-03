N = int(input())
for _ in range(N):
    S = input()
    l = u = h = 0
    for c in S:
        if c.islower(): l += 1
        elif c.isupper(): u += 1
        elif c == '-': h += 1
    if l >= u and len(S) <= 10 and l+u+h > 0:
        print(S)
        break