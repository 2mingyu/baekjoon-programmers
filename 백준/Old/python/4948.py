"""
베르트랑 공준
"""
p = [1] * (123456*2+1)
p[1] = 0
for i in range(2, 123456*2+1):
    if p[i]:
        n = i * 2
        while n <= 123456*2:
            p[n] = 0
            n += i

while True:
    n = int(input())
    if not n: break
    count = 0
    for i in range(n+1, 2*n+1):
        if p[i]: count += 1
    print(count)