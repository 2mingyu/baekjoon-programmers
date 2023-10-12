"""
5차 전직
a(i)가 작은 퀘스트 먼저
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
result = 0
activated = 0
for ai in a:
    result += activated * ai
    if activated < k: activated += 1
print(result)