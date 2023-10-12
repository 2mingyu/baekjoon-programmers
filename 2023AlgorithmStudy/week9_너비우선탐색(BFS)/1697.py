"""
숨바꼭질
"""
def find(a, b):
    second = 0
    if a == b:
        return second
    position[a] = True
    now = []
    if a-1 >= 0 and not position[a-1]: now.append(a-1)
    if a+1 <= 100000 and not position[a+1]: now.append(a+1)
    if a*2 <= 100000 and not position[a*2]: now.append(a*2)
    second += 1
    while True:
        next = []
        for i in now:
            position[i] = True
            if i == b:
                return second
            else:
                if i-1 >= 0 and not position[i-1]: next.append(i-1)
                if i+1 <= 100000 and not position[i+1]: next.append(i+1)
                if i*2 <= 100000 and not position[i*2]: next.append(i*2)
        now = next
        second += 1
N, K = map(int, input().split())
position = [False for _ in range(100000+1)]
print(find(N, K))