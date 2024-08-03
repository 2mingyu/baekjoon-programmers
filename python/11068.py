"""
회문인 수

회문 확인에 반만 확인해도 되는데 최적화는 나중에
"""
def f(n):
    for i in range(2, 65):
        t = n
        l = []
        while t != 0:
            l.append(t % i)
            t //= i
        if l[::1] == l[::-1]:
            return 1
    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    print(f(N))