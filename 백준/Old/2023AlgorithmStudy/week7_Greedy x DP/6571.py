"""
피보나치 수의 개수
"""
f = [1, 2]
while f[-1] < 10**100:
    f.append(f[-1] + f[-2])
while True:
    a, b = map(int, input().split())
    if a +b == 0: break
    result = 0
    for i in f:
        if a <= i <= b: result +=1
        elif i > b: break
    print(result)