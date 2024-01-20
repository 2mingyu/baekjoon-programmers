"""
와그와글 숭고한
"""
S, K, H = map(int, input().split())
if S+K+H >= 100: print('OK')
else:
    M = min(S, K, H)
    if S == M: print('Soongsil')
    elif K == M: print('Korea')
    elif H == M: print('Hanyang')