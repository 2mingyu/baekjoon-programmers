"""
건공문자열

시간 초과
N, K = map(int, input().split())
S = [''] + list(input())
for i in range(1, N-K+2):
    S[i:i+K] = S[i+K-1:i-1:-1]
print(''.join(S))

CPUOS
PCUOS
PUCOS
PUOCS
PUOSC

CPUOS
UPCOS
UOCPS
UOSPC

CPUOS
OUPCS
OSCPU

CPUOS
SOUPC
"""
N, K = map(int, input().split())
S = [''] + list(input())
if (N-K)%2: print(''.join(S[K:N+1]) + ''.join(S[1:K]))
else: print(''.join(S[K:N+1]) + ''.join(S[K-1:0:-1]))