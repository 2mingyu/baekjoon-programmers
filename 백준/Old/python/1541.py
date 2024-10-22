"""
잃어버린 괄호
마이너스와 마이너스 사이에 있는 플러스를 먼저
"""
s = input().split('-')
r = sum(list(map(int, s[0].split('+'))))
for ss in s[1:]:
    l = list(map(int, ss.split('+')))
    r -= sum(l)
print(r)