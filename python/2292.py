"""
벌집
1 2 3  4  5
1~7~19~37~61
 6 12 18 24
"""
N = int(input())
result = 1
now = 1
while now < N:
    now += result*6
    result += 1
print(result)