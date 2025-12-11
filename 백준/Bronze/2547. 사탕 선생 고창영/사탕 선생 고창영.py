T = int(input())
for _ in range(T):
    input()
    N = int(input())
    s = sum([int(input()) for _ in range(N)])
    print(['YES', 'NO'][s%N > 0])