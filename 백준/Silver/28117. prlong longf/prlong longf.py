N = int(input())
S = input()
T = ''
i = 0
while i < N-3:
    if S[i:i+4] == 'long':
        T += 'L'
        i += 4
    else:
        T += S[i]
        i += 1
l = [1, 1]
for i in range(1, len(T)):
    t = l[-1]
    if T[i] == T[i-1] == 'L': t += l[-2]
    l.append(t)
print(l[-1])