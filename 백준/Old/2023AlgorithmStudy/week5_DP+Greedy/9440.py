"""
최대한 갯수를 반반 나눠야 자릿수가 안커짐
큰자릿수에 작은 숫자를 배치
1, 2, 7, 8, 9
3개 2개로 나누고
1__,__
12_,7_ or 17_,2_
128,79 or 129,78 or 178,29 or 179,28 모두 같다.

9, 8, 7, 2, 1
answer = 9 + 8 + 7*10 + 2*10 + 1*100

0이 맨 앞에 올 수는 없다?
0, 1, 2, 3, 4, 0, 1, 2, 3
4, 3, 3, 2, 2, 1, 1, 0, 0
4, 3, 3, 2, 2, 0, 0, 1, 1
10234 + 1023
"""
while True:
    tmp = list(map(int, input().split()))
    if tmp == [0]:
        break
    N = tmp[0]
    nums = tmp[1:]
    nums.sort(reverse = True)
    answer = 0
    num1 = []
    num2 = []
    zeros = []
    for num in nums:
        if num == 0:
            zeros.append(num)
        else:
            if len(num1) <= len(num2):
                num1.insert(0, num)
            else:
                num2.insert(0, num)
    for zero in zeros:
        if len(num1) < len(num2):
            num1.insert(1, zero)
        else:
            num2.insert(1, zero)
    n1 = ''
    n2 = ''
    for n in num1:
        n1 += str(n)
    for n in num2:
        n2 += str(n)
    print(int(n1) + int(n2))