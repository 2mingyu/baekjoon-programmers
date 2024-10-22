"""
IT Passport Examination
"""
N = int(input())
for _ in range(N):
    i, S, M, T = map(int, input().split())
    j = S+M+T
    print(i, j, ['FAIL', 'PASS'][j >= 55 and S >= 30*0.35 and M >= 30*0.25 and T >= 30*0.4])