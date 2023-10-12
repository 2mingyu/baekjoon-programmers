N = int(input())
cards = list(range(1, N + 1))
front = 0
while front != len(cards) - 1:
    # cards.pop(0)
    # cards.append(cards.pop(0))
    # a.pop(0)의 시간복잡도 O(n), a.append(x)의 시간복잡도 O(1)
    front += 1
    cards.append(cards[front])
    front += 1
print(cards[front])