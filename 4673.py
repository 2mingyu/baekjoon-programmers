"""
셀프 넘버

def get_nextNumber(n):
    nextNumber = n
    while n > 0:
        nextNumber += n % 10
        n //= 10
    return nextNumber
"""
def get_nextNumber(n):
    return n + sum(map(int, str(n)))

isSelfNumber = [False] * 10001
for i in range(1, 10001):
    nextNumber = get_nextNumber(i)
    while nextNumber <= 10000 and not isSelfNumber[nextNumber]:
        isSelfNumber[nextNumber] = True
        nextNumber = get_nextNumber(nextNumber)
for i in range(1, 10001):
    if not isSelfNumber[i]: print(i)