"""
Is the Name of This Problem
"""
while True:
    S = input()
    if S == 'END': break
    if S[0] == '\"':
        A = ''
        for i in range(1, len(S)):
            if S[i] == '\"': break
            A += S[i]
        if S == '\"' + A + '\" ' + A:
            print('Quine(' + A + ')')
            continue
    print('not a quine')