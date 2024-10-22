"""
Pizza
"""
n = int(input())
for _ in range(n):
    A1, P1 = map(int, input().split())
    R1, P2 = map(int, input().split())
    print(['Whole pizza', 'Slice of pizza'][A1/P1 > (R1*R1*3.14)/P2])