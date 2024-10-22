N, K = map(int, input().split())
results = []
k = 0
people = list(range(1, N + 1))
while len(people):
    k += K - 1
    if k >= len(people):
        k %= len(people)
    results.append(people.pop(k))
print("<" + str(results)[1:-1] + ">")