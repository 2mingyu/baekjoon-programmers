while True:
    n = int(input())
    if not n: exit()
    l = [int(input()) for _ in range(n)]
    for e in l[::-1]:
        print(e)
    print(0)