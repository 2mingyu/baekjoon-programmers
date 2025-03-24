N = int(input().strip())
S = input()

pi = [0] * N
j = 0
for i in range(1, N):
    while j > 0 and S[i] != S[j]:
        j = pi[j-1]
    if S[i] == S[j]:
        j += 1
        pi[i] = j

b = pi[-1]
p = N - b
print(1+(N-1)//p)