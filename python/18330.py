"""
Petrol
"""
n = int(input())
k = int(input()) + 60
m = 0
if n >= k: n, m = k, n-k
print(n*1500 + m*3000)