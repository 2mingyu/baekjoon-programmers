"""
큰 수 만들기

== 3 30 34 5 9
=> 9 5 34 3 30

== 34 3 30 을 어떻게 만들까 ..
=> 34 3(3) 30

== 34 3 30 35 351 352 353 354 355 356
=> 356 355 354 35(3) 353 352 351 34(3) 3(33) 30(3)
=>             35(35) 353(3)

처음에 틀린 이유: N 범위가 1000 이하인데 리스트 안의 숫자 범위가 1000 이하인줄 ..
"""
N = int(input())
A = input().split()
B = []
for a in A:
    b = ''
    i = 0
    while len(b) < 9:
        b += a[i%len(a)]
        i += 1
    B.append(int(b))

C = [x for _, x in sorted(zip(B, A), reverse=True)]
if C[0] == '0': print(0)
else: print(''.join(C))