"""
피노키오
"""
L = int(input())
S = input()
d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for c in S: d[c] += 1
print(d['A'] * d['C'] * d['G'] * d['T'] % 1000000007)