"""
Molar mass
"""
W = {'C': 12.01,
     'H': 1.008,
     'O': 16.00,
     'N': 14.01}

T = int(input())
for _ in range(T):
    S = input()
    r = 0
    i = 0
    while i < len(S):
        try:
            n = int(S[i+1:i+3])
            r += W[S[i]] * n
            i += 3
        except:
            try:
                n = int(S[i+1])
                r += W[S[i]] * n
                i += 2
            except:
                n = 1
                r += W[S[i]] * n
                i += 1
    print("%.3f" %r)