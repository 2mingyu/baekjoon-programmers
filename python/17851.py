"""
This Problem's a Slam Dunk
"""
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = 0
for i in range(5):
    if a[i] > b[i]: c += 1
print(c)