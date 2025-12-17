import math
N = int(input())
x = list(map(int, input().split()))
l = sorted([y*2 for y in x])
print(math.lcm(*l))