N = int(input())
l = [input() for _ in range(N)]
r = 0
for i in range(N):
    for j in range(i+1, N):
        S, T = l[i], l[j]
        for k in range(1, min(len(S), len(T))+1):
            if S[len(S)-k:] == T[:k] or T[len(T)-k:] == S[:k]:
                r += 1
                break
print(r)