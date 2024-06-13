"""
2023은 무엇이 특별할까?
"""
T = int(input())
for _ in range(T):
  N = int(input())
  print(['Good', 'Bye'][bool((N+1) % (N%100))])