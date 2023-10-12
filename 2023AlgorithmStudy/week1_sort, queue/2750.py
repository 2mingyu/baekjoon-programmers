n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(input()))
for i in range(n):
    for j in range(i, n):
        if n_list[i] > n_list[j]:
            tmp = n_list[i]
            n_list[i] = n_list[j]
            n_list[j] = tmp
for i in range(n):
    print(n_list[i])