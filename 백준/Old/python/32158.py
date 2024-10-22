"""
SWAPC
"""
N = int(input())
S = list(input())
P = []
C = []
for i in range(N):
    if S[i] == 'P': P.append(i)
    elif S[i] == 'C': C.append(i)
for i in range(min(len(P), len(C))):
    S[P[i]] = 'C'
    S[C[i]] = 'P'
print(''.join(S))