#coding=utf-8
import numpy as np

'''
最长公共子串(The Longest Common Substring),要求连续。使用一个矩阵来记录两个字符串中所有位置的两个字符之间的匹配情况，如果匹配上了，则
该位置记为1，否则为0。最后求出对角线最长的从1开始的每次增加1的序列，其对应的位置就是最长匹配字串的位置。
'''
def find_lcsubstr(s1,s2):
    #   创建大小为len(s2)*len(s1)的0矩阵，为方便计算，多初始化一行一列
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    #   最长匹配的长度
    maxnum = 0
    #   最长匹配在s1中的最后一位位置
    p = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i+1][j+1]=m[i][j]+1
                if m[i+1][j+1]>maxnum:
                    maxnum=m[i+1][j+1]
                    p = i+1
    print('\n'.join(map(str,m)))
    return s1[p-maxnum:p],maxnum

'''
最长公共子序列(The Longest Common Subsequence),不要求连续。初始化两个矩阵，其中一个记录两个字符串中匹配的情况，如果
匹配上了则将左上方的值加1，否则该位置为左上方和上方两个值中的最大值；另外一个矩阵记录矩阵转移方向，然后根据转移方向，回
溯找到最长子序列。
'''
def find_lcseque(s1, s2):
    #   创建大小为len(s2)*len(s1)的0矩阵，为方便计算，多初始化一行一列
    m = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
    #   创建相同大小的空矩阵，用来记录转移方向
    d = [[None for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]

    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            #   字符匹配成功，则该位置的值等于左上方的值加1
            if s1[p1] == s2[p2]:
                m[p1 + 1][p2 + 1] = m[p1][p2] + 1
                d[p1 + 1][p2 + 1] = 'ok'
            #   左值大于上值，则该位置的值为左值，并标记方向为left
            elif m[p1 + 1][p2] > m[p1][p2 + 1]:
                m[p1 + 1][p2 + 1] = m[p1 + 1][p2]
                d[p1 + 1][p2 + 1] = 'left'
            #   上值大于左值，则该位置的值为上值，并标记方向为up
            else:
                m[p1 + 1][p2 + 1] = m[p1][p2 + 1]
                d[p1 + 1][p2 + 1] = 'up'
    (p1, p2) = (len(s1), len(s2))
    print('\n'.join(map(str,d)))
    s = []
    while m[p1][p2]:
        c = d[p1][p2]
        #   匹配成功，插入该字符，并向左上角找下一个
        if c == 'ok':
            s.append(s1[p1 - 1])
            p1 -= 1
            p2 -= 1
        #   未匹配成功，则根据标记向左找下一个
        if c == 'left':
            p2 -= 1
        #   未匹配成功，则根据标记向上找下一个
        if c == 'up':
            p1 -= 1
    s.reverse()
    return ''.join(s)

if __name__ == '__main__':
    s1 = 'abcdefghijklmn'
    s2 = 'aaabcdefhijllm'
    lcsubstr,maxnum = find_lcsubstr(s1,s2)
    print('最长公共子串： %s, 长度： %d'%(lcsubstr,maxnum))
    print('--------------------------------------------')
    lcseque = find_lcseque(s1,s2)
    print('最长公共子序列： %s'%lcseque)
