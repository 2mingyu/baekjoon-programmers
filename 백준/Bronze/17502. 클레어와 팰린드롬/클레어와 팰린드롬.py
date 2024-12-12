N = int(input())
S = list(input())

for i in range(N // 2):
    if S[i] == '?' and S[N - i - 1] == '?':
        S[i] = S[N - i - 1] = 'a'
    elif S[i] == '?':
        S[i] = S[N - i - 1]
    elif S[N - i - 1] == '?':
        S[N - i - 1] = S[i]

if N % 2 == 1 and S[N // 2] == '?':
    S[N // 2] = 'a'

print(''.join(S))
