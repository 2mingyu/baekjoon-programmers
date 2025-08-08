N, M = map(int, input().split())
print(N*2 if N==M else min(N, M)*2+1)