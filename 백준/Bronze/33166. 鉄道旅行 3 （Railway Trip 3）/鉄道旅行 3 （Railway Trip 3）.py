P, Q = map(int, input().split())
A, B = map(int, input().split())
print(min(P, Q)*A + max(Q-P, 0)*B)