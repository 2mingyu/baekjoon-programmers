import sys
input = sys.stdin.readline
print(sum([int(input())-1 for _ in range(int(input()))])+1)