"""
Koszykarz
"""
k, w, m = map(int, input().split())
print((w-k)//m + bool((w-k)%m))