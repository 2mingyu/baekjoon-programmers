S = input()
print(S[0], end='')
for i in range(1, len(S)):
    if S[i] != S[i-1]: print(S[i], end='')