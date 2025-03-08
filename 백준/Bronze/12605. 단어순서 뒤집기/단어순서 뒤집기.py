N = int(input())
for i in range(N):
    print('Case #'+str(i+1)+':', *input().split()[::-1])