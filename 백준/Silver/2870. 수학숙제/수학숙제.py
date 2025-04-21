N = int(input())
l = []
for _ in range(N):
    S = input() + ' '
    t = ''
    for i in range(len(S)):
        if S[i] in '1234567890':
            t += S[i]
        else:
            if t:
                l.append(int(t))
                t = ''
for e in sorted(l): print(e)