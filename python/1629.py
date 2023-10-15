"""
곱셈
"""
A, B, C = map(int, input().split())
def func(a, n):
    if n == 1: return a % C
    else:
        if n%2:
            return func(a,n//2)**2*a % C
        else:
            return func(a,n//2)**2 % C
print(func(A,B))