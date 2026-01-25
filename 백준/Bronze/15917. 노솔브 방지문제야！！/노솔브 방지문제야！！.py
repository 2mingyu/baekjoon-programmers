import sys
for _ in range(int(input())):a=int(sys.stdin.readline());print(int(a&(~a+1)==a))