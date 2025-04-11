# 경사로 놓을 수 있는지
def available(l, h, t):
    for i in range(L):
        if l[i] != h or t[i]:
            return False
    return True

def check(l):
    i = 0
    t = [False] * N # 경사로 놓여 있는지
    while i < N:
        h = l[i]
        if i == N-1:
            break
        if l[i+1] == h:
            i += 1
        elif l[i+1] == h+1:
            if i-L+1 >= 0 and available(l[i-L+1:i+1], h, t[i-L+1:i+1]):
                t[i-L+1:i+1] = [True] * L
                i += 1
            else:
                return False
        elif l[i+1] == h-1:
            if i+L < N and available(l[i+1:i+1+L], h-1, t[i+1:i+1+L]):
                t[i+1:i+1+L] = [True] * L
                i += L
            else:
                return False
        else:
            return False
    return True


N, L = map(int, input().split())
M1 = [list(map(int, input().split())) for _ in range(N)]
M2 = [[] for _ in range(N)]
r = 0
for i in range(N):
    for j in range(N):
        M2[j].append(M1[i][j])

for i in range(N):
    l = M1[i]
    r += check(l)
    l = M2[i]
    r += check(l)

print(r)