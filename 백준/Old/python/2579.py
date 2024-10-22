"""
계단 오르기
한칸 올라갔으면, 다음엔 반드시 두칸 올라가야함
두칸 올라갔으면, 다음엔 한칸or두칸 올라가야함

거꾸로 생각?
한칸 내려갔으면, 다음엔 반드시 두칸 내려가야함
두칸 내려갔으면, 다음엔 한칸or두칸 내려가야함

현재 칸에 올 수 있는건
두칸 전에서 두칸올라오기
세칸 전에서 두칸+한칸올라오기
세칸 전에서 한칸+두칸올라오기는 두칸 전에서 두칸올라오기에 포함됨
https://bio-info.tistory.com/158
"""
n=int(input())
s=[int(input())for _ in range(n)]
if n<3:print(sum(s))
else:
    dp=[0]*n
    dp[0]=s[0]
    dp[1]=s[0]+s[1]
    for i in range(2,n):dp[i]=max(dp[i-3]+s[i-1]+s[i],dp[i-2]+s[i])
    print(dp[-1])