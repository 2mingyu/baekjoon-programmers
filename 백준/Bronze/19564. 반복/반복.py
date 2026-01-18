S = input()
K = 1
for i in range(1, len(S)):
    if S[i] <= S[i-1]:
        K += 1
print(K)