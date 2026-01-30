C, K, P = map(int, input().split())
print(sum([K*n+P*n**2 for n in range(C+1)]))