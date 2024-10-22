"""
우유가 넘어지면?
"""
d = {
    '.': '.',
    'O': 'O',
    '-': '|',
    '|': '-',
    '/': '\\',
    '\\': '/',
    '^': '<',
    '<': 'v',
    'v': '>',
    '>': '^',
}
N, M = map(int, input().split())
l = [input() for _ in range(N)]
for i in range(M-1, -1, -1):
    for j in range(N):
        print(d[l[j][i]], end="")
    print()