t1, m1, t2, m2 = map(int, input().split())
m = (t2*60 + m2) - (t1*60 + m1)
if m < 0:
    m += 24*60
n = m // 30
print(m, n)