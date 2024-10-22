"""
알파벳 찾기
"""
a = [-1] * 26
S = input()
for i in range(len(S)):
    if a[ord(S[i])-97] == -1: a[ord(S[i])-97] = i
for r in a: print(r, end=" ")