N=int(input().split()[0])
print(*[N if N+1<2*i else 1for i in map(int,input().split())])