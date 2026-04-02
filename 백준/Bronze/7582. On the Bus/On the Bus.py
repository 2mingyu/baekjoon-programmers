import sys
input = sys.stdin.readline

while True:
    line = input().split()
    route, Z = line[0], int(line[1])
    if route == '#':
        break
    P = int(input())
    S = int(input())
    for _ in range(S):
        off, on = map(int, input().split())
        P -= off
        P += min(on, Z - P)
    print(route, P)