N, b = map(int, input().split())
print(['no', 'yes'][N <= 2**(b+1)-1])