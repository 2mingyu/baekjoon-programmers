T = int(input())
for _ in range(T):
    S = input()
    U = S[::-1]
    for i in range(len(S)):
        if S[i:] == U[:len(S)-i]:
            print(S[:i]+S[i:]+U[len(S)-i:])
            break