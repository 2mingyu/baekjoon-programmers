"""
DNA 비밀번호

231206 알고리즘 강의 수업시간 문제
"""
S, P = map(int, input().split())
DNA = input()
A, C, G, T = map(int, input().split())
d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in range(P):
    d[DNA[i]] += 1
s, e = 0, P-1
r = 0
while True:
    if d['A'] >= A and d['C'] >= C and d['G'] >= G and d['T'] >= T:
        r += 1
    e += 1
    if e == S:
        break
    d[DNA[e]] += 1
    d[DNA[s]] -= 1
    s += 1
print(r)