A, B = map(int, input().split())
s, e = min(A, B), max(A, B)
print((s+e)*(e-s+1)//2)