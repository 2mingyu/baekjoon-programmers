x,y=map(int,input().split())
print(['SUN','MON','TUE','WED','THU','FRI','SAT'][sum([y,31,28,31,30,31,30,31,31,30,31,30,31][:x])%7])