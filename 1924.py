"""
2007년
x, y = map(int, input().split())
a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
b = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
y += sum(a[:x-1])
print(y)
print(b[y%7])
"""
x,y=map(int,input().split())
print(['SUN','MON','TUE','WED','THU','FRI','SAT'][sum([y,31,28,31,30,31,30,31,31,30,31,30,31][:x])%7])