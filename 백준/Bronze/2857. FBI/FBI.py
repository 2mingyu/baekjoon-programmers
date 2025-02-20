l = [i+1 for i in range(5) if 'FBI' in input()]
print(*(l if l else ['HE GOT AWAY!']))