N2 = input()
N3 = input()
for i in range(len(N2)):
    M2 = int(N2[:i] + ('0' if N2[i] == '1' else '1') + N2[i+1:], 2)
    for j in range(len(N3)):
        if N3[j] == '0':
            M3 = int(N3[:j] + '1' + N3[j+1:], 3)
            if M2 == M3:
                print(M2)
                exit()
            M3 = int(N3[:j] + '2' + N3[j+1:], 3)
            if M2 == M3:
                print(M2)
                exit()
        if N3[j] == '1':
            M3 = int(N3[:j] + '0' + N3[j+1:], 3)
            if M2 == M3:
                print(M2)
                exit()
            M3 = int(N3[:j] + '2' + N3[j+1:], 3)
            if M2 == M3:
                print(M2)
                exit()
        if N3[j] == '2':
            M3 = int(N3[:j] + '0' + N3[j+1:], 3)
            if M2 == M3:
                print(M2)
                exit()
            M3 = int(N3[:j] + '1' + N3[j+1:], 3)
            if M2 == M3:
                print(M2)
                exit()