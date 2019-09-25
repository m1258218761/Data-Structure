#coding=utf-8
'''
最大公约数：指两个或多个整数共有约数中最大的一个
最小公倍数：两个或多个整数公有的倍数叫做它们的公倍数，其中除0以外最小的一个公倍数就叫做这几个整数的最小公倍数
二者关系：两个数之积=最小公倍数*最大公约数
'''

#   1.辗转相除法
def caculate_1(a,b):
    s = a*b
    while a%b != 0:
        a,b = b,(a%b)
    else:
        return b,s//b

#   2.更相减损法
def caculate_2(a,b):
    s=a*b
    while a != b:
        if a>b:
            a -= b
        elif a < b:
            b -= a
    else:
        return a,s//a

if __name__ == '__main__':
    a = 40
    b = 60
    max_com_div,lst_com_mult = caculate_1(a,b)
    # max_com_div,lst_com_mult = caculate_2(a,b)
    print(max_com_div,'is the maximum common divisor')
    print(lst_com_mult,'is the least common multiple')