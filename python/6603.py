"""
로또

조합 구할때 itertools의 combinations 쓸까나 ..
"""
def f(r, i, n):
    if n == 6:
        print(*r)
        return
    for j in range(i, k):
        f(r+[S[j]], j+1, n+1)

while True:
    k, *S = map(int, input().split())
    if not k: break
    f([], 0, 0)
    print()