"""
랩실에서 잘 자요

연속된 번호 K 장의 페이지를 인쇄하기 위해서는 5+2K 만큼의 잉크를 사용
잉크를 아끼기 위해서라면 잃어버리지 않은 페이지를 인쇄해도 괜찮
ex) 1페이지, 2페이지를 인쇄하면 14잉크, 1~2페이지를 인쇄하면 9잉크
ex) 1페이지, 3페이지를 인쇄하면 14잉크, 1~3페이지를 인쇄하면 11잉크
ex) 1페이지, 4페이지를 인쇄하면 14잉크, 1~4페이지를 인쇄하면 13잉크
ex) 1페이지, 5페이지를 인쇄하면 14잉크, 1~5페이지를 인쇄하면 15잉크
잃어버린 페이지 사이에 잃어버리지 않은 페이지가 둘 이하 있으면 함께 인쇄
"""
N ,M = map(int, input().split())
p = list(map(int, input().split()))
pp = []
for i in range(1, N+1):
    if i not in p:
        pp.append(i)
result = 0
for i in range(len(pp)):
    if i == 0: result += 7
    else:
        if pp[i] - pp[i-1] <= 3:
            result += (pp[i] - pp[i-1]) * 2
        else:
            result += 7
print(result)