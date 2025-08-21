T = int(input())
for x in range(1, T+1):
    N = int(input())
    n = [input() for _ in range(N)]
    for i in range(N):
        n[i] = [len({c for c in n[i] if c != ' '}), n[i]]
    n.sort(key=lambda x: (-x[0], x[1]))
    y = n[0][1]
    print(f"Case #{x}: {y}")