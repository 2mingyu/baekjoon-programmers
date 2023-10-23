"""
트리 순회

예쁜 코드는 아니다..
문자열로 리턴하고 함수 밖에서 출력하면 좋을듯
"""
N = int(input())
tree = {}
for _ in range(N):
    node, left, right = input().split()
    tree[node] = {'left': left, 'right': right}


def preorder_traversal(n):
    print(n, end="")
    if tree[n]['left'] != '.': preorder_traversal(tree[n]['left'])
    if tree[n]['right'] != '.': preorder_traversal(tree[n]['right'])


def inorder_traversal(n):
    if tree[n]['left'] != '.': inorder_traversal(tree[n]['left'])
    print(n, end="")
    if tree[n]['right'] != '.': inorder_traversal(tree[n]['right'])


def postorder_traversal(n):
    if tree[n]['left'] != '.': postorder_traversal(tree[n]['left'])
    if tree[n]['right'] != '.': postorder_traversal(tree[n]['right'])
    print(n, end="")

preorder_traversal('A')
print()
inorder_traversal('A')
print()
postorder_traversal('A')
print()