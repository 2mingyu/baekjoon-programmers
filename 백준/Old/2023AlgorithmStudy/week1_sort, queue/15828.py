import sys

N = int(input())
Router = []
front = 0
back = 0
while True:
    information = int(sys.stdin.readline())
    if information == -1:
        break
    elif information == 0:
        front += 1
    else:
        if back - front < N:
            Router.append(information)
            back += 1
        else:
            pass
if front == back:
    print("empty")
else:
    while front < back:
        print(Router[front], end=" ")
        front += 1