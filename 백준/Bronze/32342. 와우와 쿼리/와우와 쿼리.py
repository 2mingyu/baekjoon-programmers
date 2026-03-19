Q = int(input())
for _ in range(Q):
    S = input()
    r = 0
    for i in range(len(S)-2):
        r += S[i:i+3] == 'WOW'
    print(r)