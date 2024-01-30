"""
두 용액

2467 용액
"""
def f():
    r1 = r2 = 0
    m = float('INF')
    for i in range(N):
        left, right = i+1, N-1
        while left <= right:
            mid = (left+right) // 2
            s = A[i] + A[mid]
            if s == 0:
                return i, mid
            elif s < 0:
                if abs(s) < m:
                    m = abs(s)
                    r1, r2 = i, mid
                left = mid + 1
            else:
                if abs(s) < m:
                    m = abs(s)
                    r1, r2 = i, mid
                right = mid - 1
    return r1, r2

N = int(input())
A = sorted(list(map(int, input().split())))
index = f()
print(A[index[0]], A[index[1]])