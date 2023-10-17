"""
파티가 끝나고 난 뒤
"""
L, P = map(int, input().split())
for i in list(map(int, input().split())):
    print(i-L*P, end=" ")