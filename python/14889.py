"""
스타트와 링크

맞긴 했는데 최적화된 해답은 아닌듯.
start랑 link랑 반대로 나오는 경우는 없애줘야되는데 안했음
"""
def make_team(s, n):
    if n == 0:
        calc(s)
    else:
        for i in range(s[-1]+1, N):
            make_team(s+[i], n-1)

def calc(s):
    global result
    start = link = 0
    l = [i for i in range(N) if i not in s]
    for i in range(N//2):
        for j in range(i+1, N//2):
            start += S[s[i]][s[j]] + S[s[j]][s[i]]
            link += S[l[i]][l[j]] + S[l[j]][l[i]]
    result = min(result, abs(start-link))

N = int(input())
S = []
for _ in range(N): S.append(list(map(int, input().split())))
result = float('INF')
for i in range(N//2): make_team([i], N//2-1)
print(result)