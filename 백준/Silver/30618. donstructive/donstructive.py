N = int(input())
print(' '.join(map(str, [i for i in range(2, N+1, 2)] + [i for i in range(1, N+1, 2)][::-1])))