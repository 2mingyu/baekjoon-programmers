n = int(input())
print(int(n > 0 and (n & (n - 1)) == 0))