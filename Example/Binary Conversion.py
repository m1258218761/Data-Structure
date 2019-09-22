#coding=utf-8

#   n是需要转换的数字，k是当前进制，j是目标进制,支持2-36进制
def trans(n,k,j):
    _map = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'
        ,'P','Q','R','S','T' ,'U','V','W','X','Y','Z']
    #   先将其他进制转为十进制,可以直接使用python内置函数int，也可以使用自定义函数进行转换
    # n = int(n,k)
    n = trans_to_ten(n,k,_map)
    #   再将十进制数转换为其他进制数
    result = []
    while n != 0:
        y = n % j
        n = n // j
        result.append(_map[y])
    result.reverse()
    return ''.join(result)

#   将其他进制的数转换为十进制，n为需要转换的数字，k为当前进制
def trans_to_ten(n,k,_map):
    result = 0
    for i in range(len(n)):
        result += _map.index(n[i])*(k**(len(n)-i-1))
    return result

if __name__ == '__main__':
    print(trans('25',10,13))
