"""
최소 스패닝 트리

간선을 가중치 작은 순으로 정렬
A, B가 같은 부모가 아닐 때 간선 추가
"""
"""
import sys
input = sys.stdin.readline

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
    parent_A, parent_B = A, B
    # print(A,B,C)
    while True:
        if parent_A == parent[parent_A]: break
        tmp = parent_A
        parent_A = parent[parent_A]
        parent[tmp] = parent_A
    while True:
        if parent_B == parent[parent_B]: break
        tmp = parent_B
        parent_B = parent[parent_B]
        parent[tmp] = parent_B
    if parent_A != parent_B:
        parent[parent_B] = parent_A
        weights += C
    # print(parent)
print(weights)

시간초과 ..
"""
"""
import sys
input = sys.stdin.readline

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
edges.sort(key = lambda x: x[2])
for edge in edges:
    A, B, C = edge
    parent_A = get_parent(A)
    parent_B = get_parent(B)
    if parent_A != parent_B:
        if parent_A < parent_B: parent[parent_B] = parent_A
        else: parent[parent_A] = parent_B
        weights += C
print(weights)

231214에 풀었는데 재채점 됨? Recursion Error
"""
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