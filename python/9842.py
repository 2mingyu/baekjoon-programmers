"""
Prime
"""
n = int(input())
c = 0
p = [1] * 150000
p[0] = p[1] = 0
for i in range(150000):
    if p[i] == 1:
        c += 1
        if c == n:
            print(i)
            exit()
        t = i + i
        while t < 150000:
            p[t] = 0
            t += i
