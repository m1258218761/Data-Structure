#coding=utf-8
'''动态规划解决0/1背包问题'''
def back():
    N = 6
    W = 21
    B = [[0 for x in range(21)] for i in range(6)]
    w = [0,2,3,4,5,9]
    v = [0,3,4,5,8,10]
    k=1
    while k<N:
        C = 1
        while C<W:
            if w[k] > C:
                B[k][C] = B[k-1][C]
            else:
                value1 = B[k-1][C-w[k]] + v[k]
                value2 = B[k-1][C]
                if value1 > value2:
                    B[k][C] = value1
            C += 1
        k += 1
    return B
if __name__ == '__main__':
    B=back()
    print('\n'.join(map(str,B)))
    print(B[5][20])