t = {
    'A': {'A': 'A', 'G': 'C', 'C': 'A', 'T': 'G'},
    'G': {'A': 'C', 'G': 'G', 'C': 'T', 'T': 'A'},
    'C': {'A': 'A', 'G': 'T', 'C': 'C', 'T': 'G'},
    'T': {'A': 'G', 'G': 'A', 'C': 'G', 'T': 'T'}
    }
N = int(input())
s = list(input())
while len(s) > 1:
    s.append(t[s.pop()][s.pop()])
print(*s)