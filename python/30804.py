"""
과일 탕후루

j-i+1 이 꽂혀있는 과일의 개수
"""
N = int(input())
S = list(map(int, input().split()))
r = 0
i = j = 0
d = {S[0]: 1}
while j < N-1:
    if len(d) <= 2:
        r = max(r, j-i+1)
        j += 1
        if S[j] in d: d[S[j]] += 1
        else: d[S[j]] = 1
    elif len(d) > 2:
        d[S[i]] -= 1
        if d[S[i]] == 0: d.pop(S[i])
        i += 1
if len(d) <= 2: r = max(r, j-i+1)
print(r)