n = int(input())
r = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        k = n-i-j
        if k >= i+j:
            continue
        else:
            if j > k:
                break
            r += 1
print(r)