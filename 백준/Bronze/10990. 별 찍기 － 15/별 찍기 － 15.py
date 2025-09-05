N = int(input())
print(' '*(N-1) + '*')
for i in range(2, N+1):
    print(' '*(N-i)+'*'+' '*((i-1)*2-1) + '*')