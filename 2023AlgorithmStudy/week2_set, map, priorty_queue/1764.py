import sys

N, M = map(int, input().split())
people = dict()
results = []
for n in range(N):
    tmp = sys.stdin.readline().strip()
    people[tmp] = n
for m in range(M):
    tmp = sys.stdin.readline().strip()
    # list, tuple의 in 연산자의 시간복잡도 O(n)
    # set, dictionary의 in 연산자의 시간복잡도 O(1)
    if tmp in people:
        results.append(tmp)
results.sort()
print(len(results))
for r in results:
    print(r)