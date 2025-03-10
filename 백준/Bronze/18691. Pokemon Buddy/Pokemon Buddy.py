T = int(input())
for _ in range(T):
    G, C, E = map(int, input().split())
    G = [1, 3, 5][G-1]
    print(max(0, E-C)*G)