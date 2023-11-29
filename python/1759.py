"""
암호 만들기
"""
L, C = map(int, input().split())
alpha = sorted(input().split())

def f(mo, ja, li, s):
    if len(s) == L:
        if mo >= 1 and ja >= 2:
            print(s)
            return
    for i in range(len(li)):
        if li[i] in 'aeiou':
            f(mo+1, ja, li[i+1:], s+li[i])
        else:
            f(mo, ja+1, li[i+1:], s+li[i])

f(0, 0, alpha, '')