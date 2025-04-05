for t in range(1, 11):
    N = int(input())
    B = list(map(int, input().split()))
    r = 0
    for i in range(2, N-2):
        r += max(0, B[i] - max(B[i-2], B[i-1], B[i+1], B[i+2]))
    print(f"#{t} {r}")