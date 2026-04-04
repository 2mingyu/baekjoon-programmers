s = input()
n = len(s)
r = None
for i in range(1, n-1):
    for j in range(i+1, n):
        t = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]
        if r is None or t < r:
            r = t
print(r)