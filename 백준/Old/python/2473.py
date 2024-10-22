"""
세 용액

2467 용액 이랑 비슷
"""
def f():
    r1 = r2 = r3 = 0
    m = float('INF')
    for i in range(N):
        for j in range(i+1, N):
            left, right = j+1, N-1
            while left <= right:
                mid = (left+right) // 2
                s = A[i] + A[j] + A[mid]
                if s == 0:
                    return i, j, mid
                elif s < 0:
                    if abs(s) < m:
                        m = abs(s)
                        r1, r2, r3 = i, j, mid
                    left = mid + 1
                else:
                    if abs(s) < m:
                        m = abs(s)
                        r1, r2, r3 = i, j, mid
                    right = mid - 1
    return r1, r2, r3

N = int(input())
A = sorted(list(map(int, input().split())))
index = f()
print(A[index[0]], A[index[1]], A[index[2]])