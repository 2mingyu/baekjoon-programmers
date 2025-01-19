l = [sum(list(map(int, input().split()))) for _ in range(5)]
m = max(l)
print((l.index(m)+1), m)