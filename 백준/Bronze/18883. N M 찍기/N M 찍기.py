N, M = map(int, input().split())
for i in range(N): print(*[i*M+j+1 for j in range(M)])