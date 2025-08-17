N, M = map(int, input().split())
S = input()
C = 0
T = ''
i = N-1
while i >= 0:
    if C == 0:
        if S[i] not in 'AEIOU':
            T += S[i]
            C += 1
    elif C == 1:
        if S[i] == 'A':
            T += S[i]
            C += 1
    elif C == 2:
        if S[i] == 'A':
            T += S[i]
            C += 1
    else:
        T += S[i]
    i -= 1
if M <= len(T):
    print('YES')
    T = T[::-1]
    print(T[len(T)-M:])
else:
    print('NO')