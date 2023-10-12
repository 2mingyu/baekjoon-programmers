"""
열 개씩 끊어 출력하기
"""
i=0
for j in input():
    print(j,end="")
    i+=1
    if not i%10: print()