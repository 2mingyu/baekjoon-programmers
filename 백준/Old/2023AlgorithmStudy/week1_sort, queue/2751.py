import sys

n = int(sys.stdin.readline())
n_list = []
for i in range(n):
    n_list.append(int(sys.stdin.readline()))
n_list.sort()
for i in range(n):
    print(n_list[i])