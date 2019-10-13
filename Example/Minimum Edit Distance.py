#coding=utf-8
import numpy as np
'''
编辑距离是用来比较两个字符串之间相似度的度量方法，表示的是两个字符串间相互转换所需要的最少步骤。
'''

def edit_distance(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    dp = np.zeros((len1 + 1, len2 + 1))
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            delta = 0 if l1[i - 1] == l2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j - 1] + delta, min(dp[i - 1][j] + 1, dp[i][j - 1] + 1))
    return dp[len1][len2]

if __name__ == '__main__':
    l1 = 'abcdefg'
    l2 = 'abccegg'
    ed = edit_distance(l1,l2)
    print(ed)