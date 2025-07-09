import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges = []
weights = 0
for _ in range(E):
    A, B, C = map(int, input().split())
    if A > B: A, B = B, A
    edges.append([A, B, C])
edges.sort(key=lambda x: x[2])
for edge in edges:
    A, B, C = edge
    parent_A = get_parent(A)
    parent_B = get_parent(B)
    if parent_A != parent_B:
        if parent_A < parent_B: parent[parent_B] = parent_A
        else: parent[parent_A] = parent_B
        weights += C
print(weights)