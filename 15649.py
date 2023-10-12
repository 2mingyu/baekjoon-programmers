"""
N과 M (1)

짧지만 재귀함수 구현 아주 오래걸림..
itertools permutations 를 import 하면 아주 쉬움
"""
def f(p,l):
    if len(p)==M:
        for q in p:print(q,end=" ")
        print()
        return
    for i in range(len(l)):f(p+[l[i]],l[0:i]+l[i+1:N])
N,M=map(int,input().split())
f([],list(range(1,N+1)))