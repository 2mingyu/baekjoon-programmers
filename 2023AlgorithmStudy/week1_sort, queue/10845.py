N = int(input())
results = []
my_queue = []
for n in range(N):
    command = input().split()
    if command[0] == "push":
        my_queue.append(int(command[1]))
    elif command[0] == "pop":
        if not len(my_queue):
            results.append(-1)
        else:
            results.append(my_queue.pop(0))
    elif command[0] == "size":
        results.append(len(my_queue))
    elif command[0] == "empty":
        if not len(my_queue):
            results.append(1)
        else:
            results.append(0)
    elif command[0] == "front":
        if not len(my_queue):
            results.append(-1)
        else:
            results.append(my_queue[0])
    elif command[0] == "back":
        if not len(my_queue):
            results.append(-1)
        else:
            results.append(my_queue[-1])
for r in results:
    print(r)