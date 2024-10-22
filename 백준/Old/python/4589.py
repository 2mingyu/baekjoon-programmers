"""
Gnome Sequencing
"""
N = int(input())
print("Gnomes:")
for _ in range(N):
    l = list(map(int, input().split()))
    print("Ordered" if l == sorted(l) or l == sorted(l, reverse=True) else "Unordered")