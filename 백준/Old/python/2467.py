"""
용액

A는 오름차순으로 입력 됨. sort 필요 없다.
left = i+1 로 하는 게 핵심 (두 용액은 서로 달라야 한다)
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
A = list(map(int, input().split()))
index = f()
print(A[index[0]], A[index[1]])