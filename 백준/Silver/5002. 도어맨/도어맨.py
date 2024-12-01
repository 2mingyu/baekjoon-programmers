from collections import deque
X = int(input())
S = deque(input() + 'XX')
W = M = 0
while S:
    if S[0] == 'W':
        if W - M < X:
            S.popleft()
            W += 1
            continue
    if S[0] == 'M':
        if M - W < X:
            S.popleft()
            M += 1
            continue
    if S[1] == 'W':
        if W - M < X:
            T = S.popleft()
            S.popleft()
            S.appendleft(T)
            W += 1
            continue
    if S[1] == 'M':
        if M - W < X:
            T = S.popleft()
            S.popleft()
            S.appendleft(T)
            M += 1
            continue
    break
print(W+M)