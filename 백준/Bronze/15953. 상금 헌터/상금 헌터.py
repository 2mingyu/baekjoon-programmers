A = [0]
for i in range(6):
    A += [[500, 300, 200, 50, 30, 10][i]] * (i+1)
B = [0]
for i in range(5):
    B += [[512, 256, 128, 64, 32][i]] * (2**i)
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(((A[a] if a < len(A) else 0) + (B[b] if b < len(B) else 0)) * 10000)