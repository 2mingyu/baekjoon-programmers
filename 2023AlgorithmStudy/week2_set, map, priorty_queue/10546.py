import sys

N = int(input())
people = dict()
for n in range(N):
    tmp = sys.stdin.readline().strip()
    if tmp in people:
        people[tmp] += 1
    else:
        people[tmp] = 1
for n in range(N - 1):
    tmp = sys.stdin.readline().strip()
    people[tmp] -= 1
for p in people:
    if people[p]:
        print(p)
        break