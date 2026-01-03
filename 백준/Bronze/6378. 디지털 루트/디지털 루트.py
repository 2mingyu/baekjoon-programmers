while True:
    N = input()
    if N == '0': break
    while len(N) > 1:
        N = str(sum(map(int, list(N))))
    print(N)