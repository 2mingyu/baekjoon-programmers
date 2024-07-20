"""
Polynesiaglot (Small2)
"""
for x in range(int(input())):
 C,V,L=map(int,input().split())
 c,v=0,V
 for _ in range(L-1):c,v=v*C,(c+v)*V
 print(f'Case #{x+1}: {(c+v)%(10**9+7)}')