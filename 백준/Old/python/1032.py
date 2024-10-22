"""
명령 프롬프트
"""
N = int(input())
p = list(input())
for _ in range(N-1):
    n = input()
    for i in range(len(p)):
        if p[i] != n[i]:
            p[i] = '?'
print(''.join(p))