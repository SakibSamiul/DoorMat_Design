def Door_mat(N, M):
    for i in range(N // 2):
        pattern = ".|." * (2 * i + 1)
        line = pattern.center(M, "-")
        
        print(line)
    line1 = "WELCOME".center(M, "-")
    print(line1)

 
    for i in range(N-2, -1, -2):
        print((i * (".|.")).center(M, "-"))
        
N, M = map(int, input().split())
Door_mat(N, M)



