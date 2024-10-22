"""
그게 무슨 코드니..
"""
S = input()
if S[0] == S[-1] == '\"' and len(S[1:-1]): print(S[1:-1])
else: print('CE')