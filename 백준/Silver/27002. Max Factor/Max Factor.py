N = int(input())
m = r = 1
for _ in range(N):
    y = x = int(input())
    i = 2
    while x > 1:
        if x % i == 0:
            x //= i
            if i > m:
                m = i
                r = y
        else:
            i += 1
print(r)