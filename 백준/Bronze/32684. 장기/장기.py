w = [13, 7, 5, 3, 3, 2]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sa = sum(x*y for x,y in zip(w,a))
sb = sum(x*y for x,y in zip(w,b)) + 1.5
print('cocjr0208' if sa > sb else 'ekwoo')