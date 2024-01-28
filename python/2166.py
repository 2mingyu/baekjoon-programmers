"""
다각형의 면적

https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0
"""
N = int(input())
p = []
for _ in range(N):
    p.append(list(map(int, input().split())))
a = b = 0
for i in range(N-1):
    a += p[i][0] * p[i+1][1]
    b += p[i][1] * p[i+1][0]
a += p[N-1][0] * p[0][1]
b += p[N-1][1] * p[0][0]
print(abs(b-a) / 2)