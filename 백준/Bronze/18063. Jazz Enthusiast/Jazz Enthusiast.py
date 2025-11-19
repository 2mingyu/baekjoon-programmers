n, c = map(int, input().split())
s = 0
for _ in range(n):
    a, b = map(int, input().split(':'))
    s += a*60+b
s -= (n-1)*c
m = s // 60
s %= 60
h = m // 60
m %= 60
h = ['', '0'][h<10] + str(h)
m = ['', '0'][m<10] + str(m)
s = ['', '0'][s<10] + str(s)
print(h+':'+m+':'+s)