"""
FizzBuzz

연속 세 개 주면 반드시 하나는 i 그대로 출력
"""
a = input()
b = input()
c = input()
i = 0
try:
    i = int(a) + 3
except:
    try:
        i = int(b) + 2
    except:
        i = int(c) + 1
r = ''
if not i%3: r += 'Fizz'
if not i%5: r += 'Buzz'
if r: print(r)
else: print(i)