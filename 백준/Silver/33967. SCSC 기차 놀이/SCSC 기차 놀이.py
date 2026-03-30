import sys
input = sys.stdin.readline

N = int(input())
s = input().strip()

room = {'][': 0, '55': 2, '22': 2}
r = 0
for i in range(N - 1):
    r += room.get(s[i:i+2], 1)
print(r)