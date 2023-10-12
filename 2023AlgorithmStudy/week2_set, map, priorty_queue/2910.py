N, C = map(int, input().split())
sequence = list(map(int, input().split()))
sequence_dict = dict()  # key=숫자, value=[등장횟수, 등장순서]
index = 0
for s in sequence:
    if s in sequence_dict:
        sequence_dict[s][0] += 1
    else:
        sequence_dict[s] = [1, index]
        index += 1
sequence_dict = sorted(sequence_dict.items(), key=lambda x:(-x[1][0], x[1][1]))
for s in sequence_dict:
    for ss in range(s[1][0]):
        print(s[0], end=" ")