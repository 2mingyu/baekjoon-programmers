"""
촌수계산
"""
def check(c):
    chon = 1
    nowSearch = l[a]
    while nowSearch:
        nextSearch = []
        for search in nowSearch:
            checked[search] = True
            if search == b: return chon
            else:
                for s in l[search]:
                    if not checked[s]: nextSearch.append(s)
        nowSearch = nextSearch
        chon += 1
    return -1

n = int(input())
l = [[] for _ in range(n+1)]
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    l[x].append(y)
    l[y].append(x)
checked = [False for _ in range(n+1)]
checked[a] = True
print(check(a))