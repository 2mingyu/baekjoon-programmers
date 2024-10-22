import itertools
N = 7
n_list_list = list(itertools.permutations(iterable=range(1, N+1), r=N))
for n_list in n_list_list:
    s = 0
    tmp = n_list[0]
    for n in n_list[1:]:
        print("(", tmp, "+", n, ")", end=" + ")
        s = s + tmp + n
        tmp = tmp + n
    print("\t= ", s)