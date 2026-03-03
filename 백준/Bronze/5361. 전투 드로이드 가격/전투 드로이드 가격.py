T = int(input())

p = [35034, 23090, 19055, 12530, 18090]

for _ in range(T):
    A, B, C, D, E = map(int, input().split())
    x = A*p[0] + B*p[1] + C*p[2] + D*p[3] + E*p[4]
    print(f"${x//100}.{x%100:02d}")