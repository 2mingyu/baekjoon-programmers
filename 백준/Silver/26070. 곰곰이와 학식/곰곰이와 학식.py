A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())
R = 0
for _ in range(3):
    T = min(A, X)
    R += T
    A -= T
    X -= T
    T = min(B, Y)
    R += T
    B -= T
    Y -= T
    T = min(C, Z)
    R += T
    C -= T
    Z -= T

    X, Y, Z = Z//3, X//3, Y//3

print(R)