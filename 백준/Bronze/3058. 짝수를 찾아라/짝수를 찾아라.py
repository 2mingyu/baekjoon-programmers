T = int(input())
for _ in range(T):
    A = sorted([x for x in map(int, input().split()) if x%2 == 0])
    print(sum(A), A[0])