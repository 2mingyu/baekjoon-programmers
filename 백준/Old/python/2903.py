"""
중앙 이동 알고리즘

N=0, 2^2
N=1, 3^2
N=2, 5^2
N=3, 9^2
N=4, 17^2
N=5, 33^2
"""
N = int(input())
x = 1
y = 3
z = 2
while x < N:
    x += 1
    y += z
    z *= 2
print(y**2)