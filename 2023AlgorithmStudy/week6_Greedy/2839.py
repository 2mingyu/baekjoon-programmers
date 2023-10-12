"""
설탕 배달
18=5+5+5+3
6=3+3
9=3+3+3
11=5+3+3
"""
N = int(input())
five = N//5
three = 0
while five >= 0:
    if (N - (five * 5)) % 3 == 0:
        three = (N - (five * 5)) // 3
        break
    five -= 1
print(five + three)