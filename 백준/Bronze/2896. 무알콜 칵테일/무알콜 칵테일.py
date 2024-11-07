A, B, C = map(int, input().split())
I, J, K = map(int, input().split())
T = min(A/I, B/J, C/K)
print(A-T*I, B-T*J, C-T*K)