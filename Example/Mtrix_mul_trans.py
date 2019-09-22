#coding=utf-8
'''python中矩阵的转置,加法，乘法实现'''

def trans(A):
  a = [[] for i in A[0]]
  for i in A:
    for j in range(len(i)):
      a[j].append(i[j])
  return a

def madd(A, B):
  if isinstance(A, (tuple, list)) and isinstance(B, (tuple, list)):
    return [[m+n for m,n in zip(i,j)] for i, j in zip(A,B)]

def matrixMul(A, B):
  return [[sum(a * b for a, b in zip(a, b)) for b in zip(*B)] for a in A]