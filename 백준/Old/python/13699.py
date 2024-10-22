"""
점화식
"""
n = int(input())
t = [1]
for i in range(1, n+1):
    s = 0
    if i % 2:
        s += t[i//2] ** 2
    for j in range(i//2):
        s += t[j] * t[i-j-1] * 2
    t.append(s)
print(t[n])