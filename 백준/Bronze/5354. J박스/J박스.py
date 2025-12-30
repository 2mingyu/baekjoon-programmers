T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1: print('#\n')
    else:
        print('#'*N)
        for _ in range(N-2):
            print('#'+'J'*(N-2)+'#')
        print('#'*N)
        print()