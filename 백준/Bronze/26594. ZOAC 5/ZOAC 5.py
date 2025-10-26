S = input()
N = 1
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        N += 1
    else:
        break
print(N)