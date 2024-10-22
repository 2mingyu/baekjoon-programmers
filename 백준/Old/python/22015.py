"""
金平糖 (Konpeito)

*a,=map(int,input().split())
print(3*max(a)-sum(a))
"""
A, B, C = map(int, input().split())
m = max(A, B, C)
print(3*m - (A + B + C))