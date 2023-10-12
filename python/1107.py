"""
리모컨
l = [100,
    'Na보다 한자리수 많으면서 가장작은숫자',
    'N과 같은자리수, N보다 크면서 가장작은숫자',
    'N과 같은자리수, N보다 작으면서 가장큰숫자'
    'N보다 한자리수 작으면서 가장큰숫자']
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
N = list(map(int, input()))
if int(input()):
    for i in input().split():
        b.remove(int(i))
# 버튼 하나도 없으면
if not b:
    print(abs(int(''.join(map(str,N)))-100))
    exit(0)
# l[0] : 100
l = [[1, 0, 0], [], [], [], []]
# l[1] : N보다 한 자리수 많으면서 가장 작은 숫자
if not b[0]:
    l[1].append(b[0])
else:
    l[1].append(b[1])
for _ in range(len(N)):
    l[1].append(b[0])
# l[2] : N과 자리수 같으면서, N보다 크면서, 가장 작은 숫자
# l[3] : N과 자리수 같으면서, N보다 작으면서, 가장 큰 숫자
i = 0
while i < len(N): # l[2], l[3]를 앞부터 N과 같은 숫자로 채워넣음
    if N[i] in b:
        l[2].append(N[i])
        l[3].append(N[i])
        i += 1
    else:
        break
if i < len(N): # l[2] : N과 같은 숫자가 없어지면, 다음자리는 N보다 크게 넣고, 나머지는 가장 작은 숫자들로 넣기
    for j in b:
        if j > N[i]:
            l[2].append(j)
            break
    for j in b[::-1]:
        if j < N[i]:
            l[3].append(j)
            break
while len(l[2]) < len(N):
    l[2].append(b[0])
while len(l[3]) < len(N):
    l[3].append(b[-1])
# l[4] : N보다 한 자리수 작으면서, 가장 큰 숫자
for _ in range(len(N)-1):
    l[4].append(b[-1])

r = abs(int(''.join(map(str,N)))-int(''.join(map(str,l[0]))))
for ll in l[1:]:
    if ll:
        r = min(r, len(ll)+abs(int(''.join(map(str,N)))-int(''.join(map(str,ll)))))
print(r)

개고생해서 가까운 숫자 찾기 했는데, 그냥 브루트포스로 푸니까 넘어갔음
"""

b = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
N = int(input())
if int(input()):
    for i in input().split():
        b.remove(int(i))
r = abs(N - 100)
for i in range(1000000):
    c = True
    for ii in str(i):
        if int(ii) not in b:
            c = False
            break
    if c:
        r = min(r, len(str(i)) + abs(N-i))
print(r)