S = input()
t = S[0]
r = 0
for i in range(1, len(S)):
    if int(S[i]) == int(t[-1]) + 1:
        t += S[i]
    else:
        if len(t) == 3: r += 1
        t = S[i]
if len(t) == 3: r += 1
print(r)