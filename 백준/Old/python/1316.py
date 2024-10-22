"""
그룹 단어 체커
"""
N = int(input())
for _ in range(N):
    w = input()
    g = [w[0]]
    for c in w:
        if c != g[-1]:
            if c in g[:-1]:
                N -= 1
                break
            else: g.append(c)
print(N)