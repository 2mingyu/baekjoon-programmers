"""
10 -4 3 1 5 6 -35 12 21 -1
10 check
-4 -> 6
3 -> 9
1 -> 10
5 -> 15
6 -> 21
-35... 21-35가 0보다 작으니 버리기?
여태까지 최대 = 21
12+21=33
-1... 뒤에 큰 수가 나올 수도 있는데?
마이너스를 기준으로 앞뒤로 나눠서 합치기?
앞에서 부터 읽었을 때 마이너스가 등장했을 때 음수가 되지 않으면 포함시키기?
21과 -35가 비교됐을 때 ..

2 1 -4 3 4 -4 6 5 -5 1
2 check
2+1 = 3
3과 -4가 더해질 때 .. 현재까지 최대는 3인데 3-4는 음수 되니까 최대값으로 3 저장
3 check
3+4 = 7
7과 -4가 더해질 때 .. 최대값으로 7 저장해두고 7-4=3인 상태로 더해나가기?
3+6 = 9
9+5 = 14
14와 -5가 더해질 때 .. 최대값으로 14 저장해두고 14-5=9인 상태로 더해나가기?

-1 -2 -3
-1 check
"""
n = int(input())
num_list = list(map(int, input().split()))
max_num = num_list[0]
tmp_sum = 0
for num in num_list:
    if num < 0:
        if tmp_sum == 0:
            max_num = max(max_num, num)
        else:
            max_num = max(max_num, tmp_sum)
        if tmp_sum + num < 0:
            tmp_sum = 0
        else:
            tmp_sum += num
    else:
        tmp_sum += num

if tmp_sum == 0:
    max_num = max(max_num, num)
else:
    max_num = max(max_num, tmp_sum)
print(max_num)