"""
solved.ac

round(1.5) -> 2
round(2.5) -> 2
파이썬 기본 round 쓰면 틀림
반올림 자리가 5인 경우, 앞자리가 홀수면 올림, 짝수면 버림
https://m.blog.naver.com/PostView.nhn?blogId=herbdoc95&logNo=221574077380&proxyReferer=http:%2F%2Fblog.naver.com%2FPostView.nhn%3FblogId%3Dherbdoc95%26logNo%3D221574077380
"""
import sys
def round(num): return int(num) + (1 if num - int(num) >= 0.5 else 0)
n = int(input())
if n:
    l = sorted([int(sys.stdin.readline()) for _ in range(n)])
    c = round(n*0.15)
    print(round(sum(l[c:n-c])/(n-c*2)))
else: print(0)