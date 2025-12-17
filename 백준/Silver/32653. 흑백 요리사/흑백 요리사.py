import math
from functools import reduce
N = int(input())
x = list(map(int, input().split()))
l = sorted([y*2 for y in x])
print(reduce(math.lcm, l))