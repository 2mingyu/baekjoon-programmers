"""
별 찍기 - 9
"""
N = int(input())
for i in list(range(N))+list(range(N-2,-1,-1)):
    print(' '*i+'*'*(2*(N-i)-1)+''*i)