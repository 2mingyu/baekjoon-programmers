"""
나이순 정렬
"""
p=[]
for i in range(int(input())):
    a,b=input().split()
    p.append([int(a),b,i])
for i in sorted(p,key=lambda x:(x[0],x[2])):
    print(i[0], i[1])