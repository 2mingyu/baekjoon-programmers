from collections import deque
N = int(input())
cards = deque()
for i in range(1, N+1): cards.append(i) # 1부터 N까지 카드
while len(cards) > 1:   # 카드가 한 장 남을 때까지 반복하게 된다.
    cards.popleft() # 제일 위에 있는 카드를 버린다.
    cards.append(cards.popleft())   # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
print(cards[0])