"""
접미사 배열
"""
S = input()
l = []
for i in range(len(S)): l.append(S[i:])
for x in sorted(l): print(x)